import time

class VueMenu : 
    @staticmethod
    def afficherMenu() : 
        print(""" 
    Jeu des Daleks 


                                    --------------------------
                                    | Légende                |
                                    | space   - téléporter   |
                                    | z       - zapper       |
    1 - Facile                      | flèches - déplacements |
    2 - Intermédiaire               --------------------------
    3 - Difficile
    4 - Quitter     
            """)
    
    def afficherTaille() :
        print("""

    Choisissez la taille de votre terrain !
                                                                --------------------
        Entrez le nombre de ligne, confirmez avec Enter,        | Min lignes   : 6 |       
        puis le nombre de colonnes et confirmez a nouveau       | Min colonnes : 8 |
                                                                --------------------
        
        """)

    @staticmethod
    def afficherAuRevoir() :
             print(""" 
    Jeu des Daleks 






    
                 Au revoir!    




            """)

class VueHighScore : 
    @staticmethod
    def afficherClassement(self, tableauHS): 
        
        print(""" 
    Jeu des Daleks 
                            Classement 

     Crédits cosmiques """)#self.creditsCosmiques
                             #Afficher 1-10 selon nb de données dans fichier CSV 
        for i in range(len(tableauHS)):
            if (i < len(tableauHS)-1):
                print("\t", i+1," ", "-", "\t" * 2, tableauHS[i])
            else: 
                print("\t", i+1,"", "-", "\t" * 2, tableauHS[i])
        time.sleep(5.0)

class VueJeu : 
    @staticmethod
    def printTop(nbCol) :
        ligneTop = "\t_"
        for x in range(0,nbCol) :
            ligneTop += "___"
        ligneTop += "_"
        print(ligneTop)

    def printLigneVide(nbCol) :
        ligneVide = "\t| "
        for x in range(0, nbCol) :
            ligneVide += "  |  "
        print(ligneVide)

    def printLigneSeparation(nbCol) :
        ligneSep = "\t|"
        for x in range(0, nbCol) :
            ligneSep += "---|"
        print(ligneSep)

    def printBottom(nbCol) :
        bottom = "\t\u203e"
        for x in range(0, nbCol) :
            bottom += "\u203e\u203e\u203e"  # char upperscore
        bottom += "\u203e"
        print(bottom)

    def printLigneDamier(ligne, nbCol, cellules) :
        ligneDamier = "\t| "
        for x in range(0, nbCol) :
            ligneDamier += str(cellules[ligne][x])
            ligneDamier += " | "
        print(ligneDamier)

    def printDamier(cellules, nbLig, nbCol) :
        VueJeu.printTop(nbCol)        
        for y in range(0, nbLig) :
            VueJeu.printLigneDamier(y, nbCol, cellules)
            if y < nbLig - 1  :
                VueJeu.printLigneSeparation(nbCol)
        VueJeu.printBottom(nbCol)


    def errDeplacement() :
        print("Le deplacement est impossible, veuillez en essayer un autre.")

    def showGameOver() :
        topBoite = "\t\t|"
        for x in range(0, 13) :
            topBoite += "\u203e"  # char upperscore
        topBoite += "|"
        print(topBoite)
        print("\t\t|  GAME OVER  |")
        print("\t\t|_____________|")

    def showNextLevel(niveau) :
        if niveau < 10 :
            niveau = "0" + str(niveau)
            
        topBoite = "\t\t|"
        for x in range(0, 16) :
            topBoite += "\u203e"  # char upperscore
        topBoite += "|"
        print(topBoite)
        print("\t\t|  NEXT LEVEL " + str(niveau) +" |")
        print("\t\t|________________|")

    def show(niveau, grille,nbLig, nbCol, nbZapper, score) :
        print("\tNiveau : 0" + str(niveau) + "\tZapper : " + str(nbZapper) + "\tCredits : " + str(score))
        print()
        VueJeu.printDamier(grille, nbLig, nbCol)
        print()
        print("\tChoisissez un deplacement...")
