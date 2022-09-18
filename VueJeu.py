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
            bottom += "\u203e"
        print(bottom)

    def printLigneDamier(lig, cellules) :
        print("")

    def printDamier(cellules) :
        VueJeu.printTop()
        VueJeu.printLigneVide()
        VueJeu.printLigneSeparation()
        VueJeu.printLigneVide()
        VueJeu.printLigneSeparation()
        VueJeu.printLigneVide()
        VueJeu.printLigneSeparation()
        VueJeu.printLigneVide()
        VueJeu.printLigneSeparation()
        VueJeu.printLigneVide()
        VueJeu.printLigneSeparation()
        VueJeu.printLigneVide()
        VueJeu.printBottom()

# POUR TEST
if __name__ == "__main__" :
    grille = [] 
    VueJeu.printDamier(grille)
