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
        print("\t| " + str(cellules[ligne][0]) + " | " + str(cellules[ligne][1]) + " | "  + str(cellules[ligne][2]) + " | " + str(cellules[ligne][3]) + " | " + str(cellules[ligne][4]) + " | " + str(cellules[ligne][5]) + " | " + str(cellules[ligne][6]) + " | " + str(cellules[ligne][7]) + " |")

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

    def show(niveau, grille, nbZapper) :
        print("\tNiveau : 0" + str(niveau) + "\t Zapper : " + str(nbZapper))
        print()
        VueJeu.printDamier(grille)
        print()
        print("\tChoisissez un deplacement...")
