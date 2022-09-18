class VueJeu : 
    @staticmethod
    def printTop() :
        print("\t_________________________________")

    def printLigneVide() :
        print("\t|   |   |   |   |   |   |   |   |")

    def printLigneSeparation() :
        print("\t|---|---|---|---|---|---|---|---|")

    def printBottom() :
        bottom = "\t"
        for x in range(0, 33) :
            bottom += "\u203e"  # char upperscore
        print(bottom)

    def printLigneDamier(ligne, cellules) :
        print("\t| " + cellules[ligne][0] + " | " + cellules[ligne][1] + " | "  + cellules[ligne][2] + " | " + cellules[ligne][3] + " | " + cellules[ligne][4] + " | " + cellules[ligne][5] + " | " + cellules[ligne][6] + " | " + cellules[ligne][7] + " |")

    def printDamier(cellules) :
        VueJeu.printTop()
        VueJeu.printLigneDamier(0, cellules)
        VueJeu.printLigneSeparation()
        VueJeu.printLigneDamier(1, cellules)
        VueJeu.printLigneSeparation()
        VueJeu.printLigneDamier(2, cellules)
        VueJeu.printLigneSeparation()
        VueJeu.printLigneDamier(3, cellules)
        VueJeu.printLigneSeparation()
        VueJeu.printLigneDamier(4, cellules)
        VueJeu.printLigneSeparation()
        VueJeu.printLigneDamier(5, cellules)
        VueJeu.printBottom()

    def showGameOver() :
        topBoite = "|"
        for x in range(0, 13) :
            topBoite += "\u203e"  # char upperscore
        topBoite += "|"
        print(topBoite)
        print("|  GAME OVER  |")
        print("|_____________|")

    def showNextLevel() :
        topBoite = "|"
        for x in range(0, 14) :
            topBoite += "\u203e"  # char upperscore
        topBoite += "|"
        print(topBoite)
        print("|  NEXT LEVEL  |")
        print("|______________|")


# POUR TEST
if __name__ == "__main__" :
    grille = [] 
    for ligne in range(0, 6) :
        cellule = []
        grille.append(cellule)
        for colone in range(0, 8) :
            cellule.append(str(colone))
    VueJeu.showGameOver()
    VueJeu.showNextLevel()
