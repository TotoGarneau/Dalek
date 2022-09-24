from vuesMenu import VueMenu, VueHighScore

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
        liste = []
        listeHighScore = []
        i = 0 
        topTen = 10

        HighScoreController.ecrireScore(self, score) #Écrire le score du joueur dans le csv 
       
        with open('fichierHighScore.csv', 'r') as csv_file: #Ouvrir le csv et mettre les valeurs dans un tableau 
            for line in csv_file.readlines():
                liste.append(line)
        liste = [int(item) for item in liste] #Convertir la liste de string en liste de int 
        liste.sort(reverse=True)              #Classer du plus grand au plus petit 
        while (i < topTen): 
            i+=1 
            if (len(liste) >= i):                              
                listeHighScore += [liste[i-1]]   #Mettre dans un tableau les 10 plus grandes valeurs  
        return listeHighScore
        
    def ecrireScore(self, score): 
        score = [score]
        with open('fichierHighScore.csv', 'a', newline="") as csv_file:  #Ouvrir le fichier en "append" pour ajouter donnée
            writer = csv.writer(csv_file)               #Activer la fonction pour écrire 
            writer.writerows(map(lambda x: [x], score)) #Écrire le score 



# ** tester les contrôleurs jeu à partir des choix du menu  **  
class JeuController: 
    def start(self, choix): #choix de niveau passé en paramètre 
        if choix == 1:
            print("Niveau Facile\n")
        elif choix == 2:
            print("Niveau Intermédiaire\n")
        elif choix == 3: 
            print("Niveau Difficile\n")
        
        score = 0         #Score du joueur sera dans la variable après sa partie 
        print ("\n" * 11)
        input("appuyez sur une touche pour continuer")
        tableauHS = HighScoreController.calculClassement(self, score) #score passé en paramètre pour classement
        VueHighScore.afficherClassement(self, tableauHS)
       
        
