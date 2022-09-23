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

     Crédits cosmiques                       """)
                             #Afficher 1-10 selon nb de données dans fichier CSV 
        for i in range(len(tableauHS)):
            if (i < len(tableauHS)-1):
                print("\t", i+1," ", "-", "\t" * 2, tableauHS[i])
            else: 
                print("\t", i+1,"", "-", "\t" * 2, tableauHS[i])
        time.sleep(5.0)

