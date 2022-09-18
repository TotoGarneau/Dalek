from controlleursMenu import ControllerMenu, JeuController


if __name__ == "__main__" :
    choixQuitter = False 
    while not choixQuitter:
        controller = ControllerMenu()
        choix = controller.choisirNiveau()
        if (choix == 1 or choix ==2 or choix == 3) :  # Si choisi un des 3 niveaux au menu
            controller = JeuController()  #Appeler la classe JeuController 
            controller.start(choix)       #Appeler la fonction start de JeuController, passer le choix en paramètre
        if choix == 4 :
            choixQuitter = True

    

            

    


