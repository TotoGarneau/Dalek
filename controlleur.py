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

    def _setPosDalek(self, grille) :
        nbDalek = self.niveau * 5
        for i in range(nbDalek) :
            y = randbelow(6)
            x = randbelow(8)
            
            if grille[y][x].getEtat() == "" :
                grille[y][x].setEtat("D")
            else :
                i -= 1



    def verifToucheValide(input) :
        if len(input) < 2 :
            verif = re.search("[123456789zt]", input)
            if verif :
                return True
            else :
                return False
        else :
            return False
        


        



if __name__ == "__main__" :
    grille = [] 
    for ligne in range(0, 6) :
        cellule = []
        grille.append(cellule)
        for colone in range(0, 8) :
            cellule.append(str(colone))
    
    ControlleurJeu.verifDeplacement()