from vuesMenu import VueMenu, VueHighScore
from os.path import exists

import time
import csv 

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

 
class HighScoreController:
    def calculClassement(self, score): 
        if not exists('fichierHighScore.csv'):  
            HighScoreController.ecrireScore(self, score)
        else:
            liste = []
            with open('fichierHighScore.csv', 'r') as csv_file:
                for line in csv_file.readlines():
                    liste.append(line)
                for i in liste :  
                    if (int(i) <= 10 and score > liste[int(i)]): 
                        HighScoreController.ecrireScore(self, score)
                        break


    def ecrireScore(self, score):  #score du joueur passé en paramètre 
        score = [score]
        with open('fichierHighScore.csv', 'a', newline="") as csv_file:  #Ouvrir le fichier en "append" pour ajouter donnée
            writer = csv.writer(csv_file)               #Activer la fonction pour écrire 
            writer.writerows(map(lambda x: [x], score)) #Écrire le score 

    def genererListeClassement(self):   #Trier les scores du plus grand au plus petit 
        max = 0 
        liste = []
        with open('fichierHighScore.csv', 'r') as csv_file:
                 for line in csv_file.readlines():
                    print("en construction")
                  



# ** tester les contrôleurs jeu à partir des choix du menu  ** 
# Le choix de niveau dans le menu principal est passé en paramètre dans la fonction start de JeuController 
class JeuController: 
    def start(self, choix): #choix de niveau passé en paramètre 
        if choix == 1:
            print("Niveau Facile\n")
            print ("\n" * 13)
            input("appuyez sur une touche pour continuer")
            score = 100; #Utiliser le score final du joueur et le passer en paramètre pour calcul high score
            HighScoreController.calculClassement(self, score)
            VueHighScore.afficherClassement()
        elif choix == 2: 
            print("Niveau Intermédiaire\n")
            print ("\n" * 13)
            input("appuyez sur une touche pour continuer")
            score = 200; #Utiliser le score final du joueur et le passer en paramètre pour calcul high score
            HighScoreController.calculClassement(self, score)
            VueHighScore.afficherClassement()
        elif choix == 3: 
            print("Niveau Difficile\n")
            print ("\n" * 13)
            input("appuyez sur une touche pour continuer")
            score = 300; #Utiliser le score final du joueur et le passer en paramètre pour calcul high score
            HighScoreController.calculClassement(self,score)
            VueHighScore.afficherClassement()

        
