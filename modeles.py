class Cellule :
    def __init__(self) :
        # Case vide : ""
        # Case occupee par Doc : "W"
        # Case occupee par Feraille : "X"
        # Case occupee par Dalek : "D"
        self.etat = self.cellNeutre()

    @staticmethod
    def cellNeutre() :
        return " "

    @staticmethod
    def cellDoc() :
        return "W"

    @staticmethod
    def cellFeraille() :
        return "X"

    @staticmethod
    def cellDalek() :
        return "D"

    def setEtat(self, occupant) :         #Affectation du nouvel occupant d'une cellule
        if occupant == " " :
            self.etat = Cellule.cellNeutre()
        elif occupant == "W" :
            self.etat = Cellule.cellDoc()
        elif occupant == "X" :
            self.etat = Cellule.cellFeraille()
        elif occupant == "D" :
            self.etat = Cellule.cellDalek()

    def getEtat(self) :
        return self.etat

    def __str__(self) :
        return self.etat

class Grille :
    def __init__(self,ligne, colonne) :
        self.grille = []

        for y in range(0, ligne) :
            cellule = []
            self.grille.append(cellule)
            for x in range(0, colonne) :
                cellule.append(Cellule())

    def getCellule(self, ligne, colone) :
        return self.grille[ligne][colone]

    def setCellule(self, ligne, colone, occupant) :
        self.grille[ligne][colone] = occupant
