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

    def _initPosDoc(grille) :
        docSet = False
        while docSet == False :
            y = randbelow(6)
            x = randbelow(8)
            if grille[y][x].getEtat() == "" :
                grille[y][x].setEtat("W")
                docSet = True
    
    def _getPosDoc(grille) :
        for lig in range(0, 6) :
            for col in range(0, 8) :
                if grille[lig][col] == "W" :
                    return lig, col

    def verifToucheValide(input) :
        if len(input) < 2 :
            verif = re.search("[0123456789ztZT]", input)
            if verif :
                return True
            else :
                return False
        else :
            return False
        
    def verifDeplacementValide(self, input, grille) :
        valid = False
        posDoc = self._getPosDoc()
        ligTo = posDoc[0]
        colTo = posDoc[1]
        if self.verifToucheValide(input) :
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
                if grille[ligTo][colTo] != "X" :
                    if grille[ligTo][colTo] == "D" :
                        return -1 # code defaite
                    else :
                        grille.setCellule(ligTo, colTo, "W")
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
