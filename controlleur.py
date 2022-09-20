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
            verif = re.search("[123456789zt]", input)
            if verif :
                return True
            else :
                return False
        else :
            return False
        
    def verifDeplacementValide(self, input, grille) :
        posDoc = self._getPosDoc()
        ligDoc = posDoc[0]
        colDoc = posDoc[1]

        if self.verifDeplacementValide(input) :
            if ligDoc > 0 and ligDoc < 5 and colDoc > 0 and colDoc < 7 :
