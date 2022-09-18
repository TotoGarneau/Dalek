from vuesMenu import VueMenu

import time 

class ControllerMenu:
    def choisirNiveau(self): 
        VueMenu.afficherMenu();  #Affiche le menu principal et la légende 
        selection = input();     #Joueur fait un choix parmi les 4 
        if selection == '1' or selection =='2' or selection =='3': 
            return int(selection) 
        elif selection == '4': 
            VueMenu.afficherAuRevoir()  
            time.sleep(5.0)
            exit()
        else : 
            print("Choix invalide, veuillez recommencer")


# ** tester les contrôleurs jeu à partir des choix du menu  ** 
# Le choix de niveau dans le menu principal est passé en paramètre dans la fonction start de JeuController 
class JeuController: 
    def start(self, choix): #choix de niveau passé en paramètre 
        if choix == 1:
            print("Niveau Facile\n")
            print ("\n" * 20)
            input("appuyez sur une touche pour continuer")
        elif choix == 2: 
            print("Niveau Intermédiaire\n")
            print ("\n" * 20)
            input("appuyez sur une touche pour continuer")
        elif choix == 3: 
            print("Niveau Difficile\n")
            print ("\n" * 20)
            input("appuyez sur une touche pour continuer")
 

        
