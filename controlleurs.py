import re
import random
import time
import csv 

from typing import final
from xml.etree.ElementTree import tostring
from os.path import exists

from vues import VueMenu, VueJeu, VueHighScore
from modeles import Cellule, Grille

class ControllerMenu:
    def choisirNiveau(self): 
        VueMenu.afficherMenu();  #Affiche le menu principal et la légende 
        selection = input();     #Joueur fait un choix parmi les 4 
        if selection == '1' or selection =='2' or selection =='3': 
            return int(selection) 
        elif selection == '4': 
            VueMenu.afficherAuRevoir()  
            time.sleep(5.0)
            exit()
        else : 
            print("Choix invalide, veuillez recommencer")

class HighScoreController:
    def calculClassement(self, score):
        HighScoreController.ecrireScore(self, score) #Écrire le score du joueur 
        liste = []
        listeHighScore = []
        loopCount = 10
        i = 1 
        with open('fichierHighScore.csv', 'r') as csv_file: #Ouvrir le fichier et faire un tableau avec les 10 plus grandes valeurs
            for line in csv_file.readlines():
                liste.append(line)
        liste = [int(item) for item in liste] #Convertir la liste de string en liste de int 
        liste.sort(reverse=True)              #Classer du plus grand au plus petit 
        while (i <= loopCount):
            listeHighScore += [liste[i-1]] 
            i+=1 
        return listeHighScore
        
    def ecrireScore(self, score):  #score du joueur passé en paramètre 
        score = [score]
        with open('fichierHighScore.csv', 'a', newline="") as csv_file:  #Ouvrir le fichier en "append" pour ajouter donnée
            writer = csv.writer(csv_file)               #Activer la fonction pour écrire 
            writer.writerows(map(lambda x: [x], score)) #Écrire le score 

class ControlleurJeu :
    def __init__(self) :
        self.niveau = 1
        self.grille = Grille()
        self._initPosDoc()
        self.posDalek = self._initPosDalek()
        self.score = 0
        self.nbCreditsCosmiques = 0
        self.nbZapper = 1

    def _reInit(self) :
        self.niveau = 1
        self.grille = Grille()
        self._initPosDoc()
        self.posDalek = self._initPosDalek()
        self.score = 0
        self.nbCreditsCosmiques = 0
        self.nbZapper = 1

    def _getGrilleAffichage(self) :
        grille = []
        for ligne in range(0, 6) :
            cellule = []
            grille.append(cellule)
            for colone in range(0, 8) :
                cellule.append(self.grille.getCellule(ligne, colone))
        return grille

    def _initPosDalek(self) :
        nbDalek = self.niveau * 5
        nbDalekSet = 0
        posDalek = []
        while nbDalekSet != nbDalek :
            y = random.randrange(0, 6)
            x = random.randrange(0, 8)         
            if self.grille.getCellule(y, x) != "W" and self.grille.getCellule(y, x) != "D" :
                self.grille.setCellule(y, x, "D")
                nbDalekSet += 1
            dalek = []
            dalek.append(y)
            dalek.append(x)
            posDalek.append(dalek)

        return posDalek

    # deplacement auto des dalek vers le doc
    def _deplacementDalek(self) :
        posDoc = self._getPosDoc()
        ligDoc = posDoc[0]
        colDoc = posDoc[1]
        tour = 1
        
        for i in range(0, len(self.posDalek)) :
            ligTo = lig = self.posDalek[i][0]
            colTo = col = self.posDalek[i][1]
            if self.grille.getCellule(lig, col) == 'D' :
                # reset case d'origine
                self.grille.setCellule(lig, col, ' ')
                # Si dalek en bas a gauche 
                if ligDoc > lig and colDoc > col :
                    ligTo += 1
                    colTo += 1
                    tour = self._verifDeplacementDalek(ligTo, colTo)
                # si dalek en bas a droite
                elif ligDoc > lig and colDoc < col :
                    ligTo += 1
                    colTo -= 1
                    tour = self._verifDeplacementDalek(ligTo, colTo)
                # si dalek en haut a gauche
                elif ligDoc < lig and colDoc < col :
                    ligTo -= 1
                    colTo -= 1
                    tour = self._verifDeplacementDalek(ligTo, colTo)
                # si dalek en haut a droite
                elif ligDoc < lig and colDoc > col :
                    ligTo -= 1
                    colTo += 1
                    tour = self._verifDeplacementDalek(ligTo, colTo)
                # si dalek sur la meme ligne et a gauche
                elif ligDoc == lig and colDoc > col :
                    colTo += 1
                    tour = self._verifDeplacementDalek(ligTo, colTo)
                # si dalek sur la meme ligne et a droite
                elif ligDoc == lig and colDoc < col :
                    colTo -= 1
                    tour = self._verifDeplacementDalek(ligTo, colTo)
                # si dalek sur la meme colone et au dessus
                elif ligDoc > lig and colDoc == col :
                    ligTo += 1
                    tour = self._verifDeplacementDalek(ligTo, colTo)
                # si dalek sur la meme colone et en dessous
                elif ligDoc < lig and colDoc == col :
                    ligTo -= 1
                    tour = self._verifDeplacementDalek(ligTo, colTo)

            self.posDalek[i][0] = ligTo
            self.posDalek[i][1] = colTo

            if tour == -1 :
                return tour
        
        return tour
    
    def _verifDeplacementDalek(self, lig, col) :
        if self.grille.getCellule(lig, col) == "D" :
            self.nbCreditsCosmiques += 1
            self.grille.setCellule(lig, col, "X")
            return 1
        elif self.grille.getCellule(lig, col) == "X" :
            self.nbCreditsCosmiques += 1
            self.grille.setCellule(lig, col, "X")
            return 1
        elif self.grille.getCellule(lig, col) == "W" :
            self.grille.setCellule(lig, col, "D")
            return -1
        else :
            self.grille.setCellule(lig, col, "D")
            return 1
       
    def _initPosDoc(self) :
            y = random.randrange(0, 6)
            x = random.randrange(0, 8)
            self.grille.setCellule(y, x, "W")
    
    def _getPosDoc(self) :
        for lig in range(0, 6) :
            for col in range(0, 8) :
                if self.grille.getCellule(lig, col) == "W" :
                    return lig, col

    def _verifToucheValide(self, input) :
        if len(input) < 2 :
            # input = str(input)
            if re.search("[0-9ztZT/s]", input) :
                return True
            else :
                return False
        else :
            return False
        
    def verifDeplacementValide(self, input) :
        posDoc = self._getPosDoc()
        ligTo = posDoc[0]
        colTo = posDoc[1]

        if re.search("[0-9ztZT/s]", input) :
            match input:  
                # move bas gauche  
                case '1':
                    if ligTo < 5 and colTo > 0 : 
                        ligTo += 1
                        colTo -= 1
                    else :
                        return 0
                # move bas
                case '2':
                    if ligTo < 5 :
                        ligTo += 1
                    else :
                        return 0
                # move bas droite
                case '3' :
                    if ligTo < 5 and colTo < 7 :
                        ligTo += 1
                        colTo += 1
                    else :
                        return 0
                # move gauche
                case '4': 
                    if colTo > 0 :
                        colTo -= 1
                    else :
                        return 0
                # no move
                case '5':
                    pass
                case '0':
                    pass
                # move droite
                case '6' :
                    if colTo < 7 :
                        colTo += 1
                    else :
                        return 0
                # move haut gauche
                case '7':
                    if ligTo > 0 and colTo > 0 :
                        ligTo -= 1
                        colTo -= 1
                    else :
                        return 0
                # move haut
                case '8':
                    if ligTo > 0 :
                        ligTo -= 1
                    else :
                        return 0
                # move haut droite
                case '9':
                    if ligTo > 0 and colTo < 7 :
                        ligTo -= 1
                        colTo += 1
                    else : 
                        return 0
        else :
            return 0 

        cell = self.grille.getCellule(ligTo, colTo)
        
        if cell == 'D' :
            cell = 1
        elif cell == 'X' :
            cell = 2
        else :
            cell = 0

        if cell == 0 :
            self.grille.setCellule(posDoc[0], posDoc[1], ' ')    
            self.grille.setCellule(ligTo, colTo, 'W')
            return 1
        elif cell == 1 :
            return -1
        else :
            return 0  

    def zappeurDoc(self) :
        posDoc = self._getPosDoc()
        ligDoc = posDoc[0]
        colDoc = posDoc[1]
        if self.nbZapper > 0 :
            # utilisation d'un zapper
            self.nbZapper -= 1
            # Definition des lignes d'action du zapper
            if ligDoc == 0 :
                ligMinZap = 0
                ligMaxZap = ligDoc + 2
            elif ligDoc == 1 :
                ligMinZap = ligDoc - 1
                ligMaxZap = ligDoc + 2
            elif ligDoc == 5 :
                ligMinZap = ligDoc - 2
                ligMaxZap = 5
            elif ligDoc == 4 :
                ligMinZap = ligDoc - 2
                ligMaxZap = ligDoc + 1
            else :
                ligMinZap = ligDoc - 2
                ligMaxZap = ligDoc + 2

            if colDoc == 0 :
                colMinZap = 0
                colMaxZap = colDoc + 2
            elif colDoc == 1 :
                colMinZap = colDoc - 1
                colMaxZap = colDoc + 2
            elif colDoc == 7 :
                colMinZap = colDoc - 2
                colMaxZap = 7
            elif colDoc == 6 :
                colMinZap = colDoc - 2
                colMaxZap = colDoc + 1
            else :
                colMinZap = colDoc - 2
                colMaxZap = colDoc + 2

            for y in range(ligMinZap, ligMaxZap + 1) :
                for x in range(colMinZap, colMaxZap + 1) :
                    if self.grille.getCellule(y, x) == 'D' :
                        self.grille.setCellule(y, x, ' ')
                        self.score += 5
            
            # re init des variable
            ligMinZap = ligMaxZap = colMinZap = colMaxZap = 0

    def usageTeleporteurNiv3(self):
        posDocteur = self._getPosDoc() 
        l = posDocteur[0]
        c = posDocteur[1]
        while self.grille.getCellule(l, c) == "W":  #Tant que le docteur est à sa position actuelle
            y = random.randrange(0, 6)  # Generer une nouvelle position aléatoire 
            x = random.randrange(0, 8)  
            for i in range(0, self.niveau * 5) : 
                if (y != l and x != c) :         # Si la case d'atterissage n'est pas la position actuelle
                    if self.grille.getCellule(y, x) != "W" and self.grille.getCellule(y, x) != "X" :         
                        self.grille.setCellule(y, x, "W") #déplacer le docteur 
                        self.grille.setCellule(l, c, " ") 

    def usageTeleporteurNiv2(self):
        posDocteur = self._getPosDoc() 
        l = posDocteur[0]
        c = posDocteur[1]
        while self.grille.getCellule(l, c) == "W":  #Tant que le docteur est à sa position actuelle
            y = random.randrange(0, 6)  # Generer une nouvelle position aléatoire 
            x = random.randrange(0, 8)  
            for i in range(0, self.niveau * 5) : 
                if (y != l and x != c) :         # Si la case d'atterissage n'est pas la position actuelle
                    if self.grille.getCellule(y, x) != "W" and self.grille.getCellule(y, x) != "D" and self.grille.getCellule(y, x) != "X" :         
                        self.grille.setCellule(y, x, "W") #déplacer le docteur 
                        self.grille.setCellule(l, c, " ") 

    def usageTeleporteurNiv1(self): 
        posDocteur = self._getPosDoc() 
        l = posDocteur[0]
        c = posDocteur[1] 
        x = 0 
        y = 0 
        tour = 0 
        self._deplacementDalek() 
        bonDeplacement = 0  
        while bonDeplacement < 5:  
            bonDeplacement = 0 
            y = random.randrange(0, 6)
            x = random.randrange(0, 8) 
            for i in range(0, self.niveau * 5) :  #vérifier la position de chaque dalek au prochain déplacement
                ligne = self.posDalek[i][0]       #obtenir les coordonnées x y du prochain déplacement des daleks
                colonne = self.posDalek[i][1]
                if( abs(y - ligne) > 2)   or  ( abs(x - colonne) > 2 ): #Si case d'atterissage est 2 cases d'écart ou plus des daleks 
                    if (y != l and x != c) :                            # Si la case d'atterissage n'est pas la position actuelle
                        if self.grille.getCellule(y, x) != "W" and self.grille.getCellule(y, x) != "D" and self.grille.getCellule(y, x) != "X" :  
                                bonDeplacement += 1
        if bonDeplacement >= 5  :           
            self.grille.setCellule(y, x, "W") #déplacer le docteur 
            self.grille.setCellule(l, c, " ")                            



    def verifVictoire(self) :
        nbDalek = 0
        for y in range(0, 6) :
            for x in range(0, 8) :
                if self.grille.getCellule(y, x) == "D" :
                    nbDalek += 1
        
        if nbDalek == 0 :
            return True
        else :
            return False

    def niveauSuivant(self) :
        self.niveau += 1

    def tourJeu(self) :
        grille = self._getGrilleAffichage()
        # affichage du niveau, de la grille et du nb de zapper disponnible
        VueJeu.show(self.niveau, grille, self.nbZapper)
        
        # lire l'input du joueur
        moveInput = input()        
        if moveInput == 'z' or moveInput == 'Z':
            self.zappeurDoc()
            result = 1
        elif moveInput == ' ':
            self.usageTeleporteurNiv1()
            result = 1 
        else :
            result = self.verifDeplacementValide(moveInput)        
            if result == 1 :
                input("Voir mouvement des daleks...")
                result = self._deplacementDalek()

        grille = self._getGrilleAffichage()
        # affichage du niveau, de la grille et du nb de zapper disponnible
        VueJeu.show(self.niveau, grille, self.nbZapper)  

        return result

    def start(self) :
        choix = self.tourJeu()
        if choix == 1 :
            win = self.verifVictoire()
            if win :
                self.niveauSuivant()
                VueJeu.showNextLevel(self.niveau)
                print()
                input("Pressez une touche pour passer au niveau suivant.")
                self.grille = Grille()
                self._initPosDoc()
                self.posDalek = []
                self.posDalek = self._initPosDalek()
                self.nbZapper += 1
        elif choix == 0 :
            VueJeu.errDeplacement()
            input()
            self.start()
        elif choix == -1 :
            VueJeu.showGameOver()
            # re init si prochaine partie
            self._reInit()
            input("Pressez une touche pour revenir au menu.")
            ControllerMenu.choisirNiveau(self)
        self.start()
