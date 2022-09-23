import re
from secrets import randbelow
from VueJeu import VueJeu
import keyword

class ControlleurJeu :
    def __init__(self) :
        self.niveau = 1
        self.grille = Grille()

    def _getGrilleAffichage(self) :
        grille = []
        for ligne in range(0, 6) :
            cellule = []
            grille.append(cellule)
            for colone in range(0, 8) :
                cellule.append(self.grille.getCellule[ligne][colone])
        return grille

    def _initPosDalek(self, grille) :
        nbDalek = self.niveau * 5
        nbDalekSet = 0
        while nbDalekSet != nbDalek :
            y = randbelow(6)
            x = randbelow(8)         
            if grille[y][x].getEtat() == "" :
                grille[y][x].setEtat("D")
                nbDalekSet += 1

    # deplacement auto des dalek vers le doc
    def _deplacementDalek(self) :
        posDoc = self._getPosDoc()
        ligDoc = posDoc[0]
        colDoc = posDoc[1]
        for lig in range(0, 6) :
            for col in range(0, 8) :
                ligTo = lig
                colTo = col
                if self.grille[lig][col] == "D" :
                    # reset case d'origine
                    self.grille[lig][col].setEtat("")
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

                if tour == -1 :
                    return tour
    
    def _verifDeplacementDalek(self, lig, col) :
        if self.grille.getCellule(lig, col) == "D" :
            self.grille.setCellule(lig, col, "X")
            return 1
        elif self.grille.getCellule(lig, col) == "X" :
            self.grille.setCellule(lig, col, "X")
            return 1
        elif self.grille.getCellule(lig, col) == "W" :
            return -1


    def _initPosDoc(grille) :
        docSet = False
        while docSet == False :
            y = randbelow(6)
            x = randbelow(8)
            if grille[y][x].getEtat() == "" :
                grille[y][x].setEtat("W")
                docSet = True
    
    def _getPosDoc(self) :
        for lig in range(0, 6) :
            for col in range(0, 8) :
                if self.grille[lig][col] == "W" :
                    return lig, col

    def _verifToucheValide(input) :
        if len(input) < 2 :
            verif = re.search("[0123456789ztZT]", input)
            if verif :
                return True
            else :
                return False
        else :
            return False
        
    def verifDeplacementValide(self, input) :
        valid = False
        posDoc = self._getPosDoc()
        ligTo = posDoc[0]
        colTo = posDoc[1]
        if self._verifToucheValide(input) :
            match str(input):
                # move bas gauche
                case "1": 
                    ligTo -= 1
                    colTo -= 1
                # move bas
                case "2":
                    ligTo -= 1
                # move bas droite
                case "3":
                    ligTo -= 1
                    colTo +=1
                # move gauche
                case "4": 
                    colTo -= 1
                # no move
                case "5":
                    pass
                case "0":
                    pass
                # move droite
                case "6" :
                    colTo += 1
                # move haut gauche
                case "7":
                    ligTo += 1
                    colTo -= 1
                # move haut
                case "8":
                    ligTo -= 1
                # move haut droite
                case "9":
                    ligTo += 1
                    colTo += 1
                
            if ligTo > 0 and ligTo < 5 and colTo > 0 and colTo < 7 :
                if self.grille[ligTo][colTo] != "X" :
                    if self.grille[ligTo][colTo] == "D" :
                        return -1 # code defaite
                    else :
                        self.grille.setCellule(ligTo, colTo, "W")
                        return 1 # code tour bien deroule
            else :
                VueJeu.errDeplacement()
                return 0 # code erreur, rejouer tour

    def verifVictoire(self) :
        nbDalek = 0
        for y in range(0, 6) :
            for x in range(0, 8) :
                if self.grille[y][x].getCellule == "D" :
                    nbDalek += 1
        
        if nbDalek == 0 :
            return True
        else :
            return False

        


    def niveauSuivant(self) :
        self.niveau += 1

