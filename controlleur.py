import re
from secrets import randbelow
from Cellule import Cellule, Grille
from controlleursMenu import ControllerMenu
from VueJeu import VueJeu
import keyword

class ControlleurJeu :
    def __init__(self) :
        self.niveau = 1
        self.grille = Grille()
        self._initPosDoc()
        self.posDalek = self._initPosDalek()
        
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
        
        for i in range(0, self.niveau * 5) :
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
            self.grille.setCellule(lig, col, "X")
            return 1
        elif self.grille.getCellule(lig, col) == "X" :
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
            if re.search("[0-9ztZT]", input) :
                return True
            else :
                return False
        else :
            return False
        
    def verifDeplacementValide(self, input) :
        posDoc = self._getPosDoc()
        ligTo = posDoc[0]
        colTo = posDoc[1]

        if re.search("[0-9ztZT]", input) :
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
        VueJeu.show(self.niveau, grille, 0)
        
        # lire l'input du joueur
        moveInput = input()

        result = self.verifDeplacementValide(moveInput)
        input("Voir mouvement des daleks...")
        if result == 1 :
            result = self._deplacementDalek()  
        grille = self._getGrilleAffichage()
        # affichage du niveau, de la grille et du nb de zapper disponnible
        VueJeu.show(self.niveau, grille, 0)  

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
                self._initPosDalek()
        elif choix == 0 :
            VueJeu.errDeplacement()
            input()
            self.start()
        elif choix == -1 :
            VueJeu.showGameOver()
            # re init si prochaine partie
            self.grille = Grille()
            self._initPosDoc()
            self._initPosDalek()
            print()
            input("Pressez une touche pour revenir au menu.")
            ControllerMenu.choisirNiveau(self)

        self.start()
