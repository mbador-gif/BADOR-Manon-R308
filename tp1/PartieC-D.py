import random

mots = ["camion", "chien", "chat", "trois", "herbe"]

# PARTIE C
def choisir_mot(liste):
    # choisit un mot aléatoire dans la liste et le retourne en majuscules
    return random.choice(liste).upper() 

def masque(mot):
    # crée un masque pour le mot en remplacant chaque lettre par un tiret du bas
    return "_" * len(mot)

# Test des fonctions
#choisir_mot(mots)
#masque("camion")

# PARTIE D
def pendu():
    mot = choisir_mot(mots)         # choisit un mot aléatoire dans la liste
    mot_masque = masque(mot)        # crée un masque pour le mot choisi
    tentatives = 7                  # nombre de tentatives autorisées
    lettres_utilise = []            # liste pour stocker les lettres proposées
    erreurs = 0                     # compteur d'erreurs

    while erreurs < tentatives and mot_masque != mot:            # boucle tant que le joueur n'a pas gagné et qu'il n'épuise pas ses tentatives
        # affiche l'état du jeu
        print("\nMot à deviner :", " ".join(mot_masque))         # créer un espace entre chaque lettre du mot masqué
        print("Erreurs :", erreurs, "/", tentatives)
        print("Lettres utilisées :", " ".join(lettres_utilise))
        
        lettre = input("Proposez une lettre : ").upper()         # demande à entrer une lettre

        if len(lettre) != 1 or not lettre.isalpha():             # vérifie si l'entrée est une seule lettre
            print("Entrez une seule lettre.")
            continue
        if lettre in lettres_utilise:                            # vérifie si la lettre a déjà été proposée
            print("Vous avez déjà proposé cette lettre.")
            continue
        lettres_utilise.append(lettre)                           # ajoute la lettre à la liste des lettres utilisées

        if lettre in mot:                   # vérifie si la lettre est dans le mot
            for i in range(len(mot)):       # verifie chaque lettre du mot
                if mot[i] == lettre:
                    mot_masque = mot_masque[:i] + lettre + mot_masque[i+1:]   # remplace le tiret par la lettre proposée
            print("Bien joué !")
        else:
            print("Raté")
            erreurs += 1                    # rajoute +1 au compteur d'erreurs

    if mot_masque == mot:                  # vérifie si le joueur a gagné
        print("\nFélicitations ! Vous avez deviné le mot :", mot)
    else:
        print("\nDommage ! Le mot était :", mot)

# test de la fonction pendu()
pendu()
