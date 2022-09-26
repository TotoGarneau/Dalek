from controlleursMenu import ControllerMenu
from controlleur import ControlleurJeu



if __name__ == "__main__" :
    choixQuitter = False 
    while not choixQuitter:
        controller = ControllerMenu()
        choix = controller.choisirNiveau()
        if (choix == 1 or choix ==2 or choix == 3) :  # Si choisi un des 3 niveaux au menu
            controller = ControlleurJeu()  #Appeler la classe JeuController 
            controller.start()       #Appeler la fonction start de JeuController, passer le choix en paramÃ¨tre
        if choix == 4 :
            choixQuitter = True