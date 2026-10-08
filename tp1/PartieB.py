# importe le module random pour générer un nombre aléatoire
import random

def nombre_secret():
    debut = int(input("Entrez le début de l'intervalle : "))  # demande de saisir le début de l'intervalle
    fin = int(input("Entrez la fin de l'intervalle : "))      # demande de saisir la fin de l'intervalle
    
    nb_secret = random.randint(debut, fin)                    # génère un nombre aléatoire entre l'intervalle choisi
    gagne = False                                               # initialise la variable de gain à False

    for i in range(9):                                        # boucle pour donner 10 chances à l'utilisateur                   
        # demande de saisir un nombre dans l'intervalle
        n = int(input("Entrez un nombre entre " + str(debut) + " et " + str(fin) + " : "))  
        
        if n < debut or n > fin :                             # vérifie si le nombre entré est en dehors de l'intervalle
            print("Le nombre doit être compris entre " + str(debut) + " et " + str(fin))
        elif n < nb_secret :                                  # cas où le nombre entré est plus petit que le nombre secret
            print("Trop petit")
        elif n > nb_secret :                                  # cas où le nombre entré est plus grand que le nombre secret
            print("Trop grand")
        elif n == nb_secret :                                 # cas lorsque le nombre entré est égal au nombre secret
            print("C'est gagné") 
            gagne = True                                       
            break                                             # sort de la boucle si le joueur gagne                       
    
    if not gagne:
        print("Perdu ! Le nombre secret était " + str(nb_secret)) # affiche le nombre secret à la fin du jeu si le joueur perd                                

    if input("Voulez-vous rejouer ? (oui/non) ").lower() == "oui":  # demande à l'utilisateur s'il veut rejouer
        nombre_secret()                                        # relance la fonction si l'utilisateur veut rejouer

# test de la fonction 
nombre_secret()
