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
    def afficherClassement(): 
        
        print(""" 
    Jeu des Daleks 


                            Classement 
                            
     Crédits cosmiques                       
            """)
        chiffres = [1,2,3,4,5,6,7,8,9,10]  #Afficher 1-10 selon nb de données dans fichier CSV 
        for i in chiffres:
            if (i < 10):
                print("\t", i," ", "-", "\t" * 2, "Test")
            else :
                print("\t", i,"", "-", "\t" * 2, "Test")
        time.sleep(5.0)
        
        
    tableau = [] # Afficher les données en ordre de plus grand au plus petit du fichier CSV
    #Mettre dans le tableau les données contenues dans le fichier CSV

