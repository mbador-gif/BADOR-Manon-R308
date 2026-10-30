import random


# ------- PARTIE A -------------------------------------------------------------------------
class Grille:
    def __init__(self):

        # Création d'une grille 3x3, sel.tableau stocke les cases du jeu
        self.tableau = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ]

    
    # Permet d'afficher la grille dans notre console
    def afficher(self):
        for ligne in self.tableau:
            print(" | ".join(ligne))  # Traits verticaux
            print("---------")        # Traits horizontaux


    def jouer(self, x, y, joueur):
        if joueur not in ("X", "O"):            # Cas si le symbole n'est pas correct
            print("Symbole invalide")           
            return False

        if x < 0 or x > 2 or y < 0 or y > 2:    # Vérifie si les coordonnées existent
            print("Case hors de la grille")
            return False

        if self.tableau[x][y] != " ":           # Vérifie que la case n'est pas occupée
            print("Case déjà occupée")
            return False

        self.tableau[x][y] = joueur              # Coup du joueur
        return True


    def est_gagnant(self, j):
        # Vérifie les lignes
        for ligne in self.tableau:     # Parcours les cases d'une même ligne
            if ligne == [j, j, j]:     # Vérifie si le symbole des 3 cases est le même
                return True

        # Vérifie les colonnes
        for i in range(3):
            if (self.tableau[0][i] == j and
                self.tableau[1][i] == j and
                self.tableau[2][i] == j):
                return True

        # Vérifie la diagonale du haut gauche au bas droit
        if (self.tableau[0][0] == j and
            self.tableau[1][1] == j and
            self.tableau[2][2] == j):
            return True

        # Vérifie la diagonale du bas gauche au haut droit
        if (self.tableau[0][2] == j and
            self.tableau[1][1] == j and
            self.tableau[2][0] == j):
            return True
            
        return False


    def est_plein(self):
        for ligne in self.tableau:    # Parcours les trois lignes de la grille
            for case in ligne:        # Parcours les trois cases de chaque ligne
                if case == " ":
                    return False

        return True



# ------- PARTIE B -------------------------------------------------------------------------
class JoueurHumain:
    def prochain_coup(self, tab, symbole):
        print("C'est au tour du joueur", symbole)

        x = int(input("Choisir une ligne (0-2) : "))     # Choisir la ligne à jouer
        y = int(input("Choisir une colonne (0-2) : "))   # Choisir la colonne à jouer

        return (x, y)

   
class JoueurIA:
    def prochain_coup(self, tab, symbole):
        cases_libres = []                         # Création d'une liste vide

        # Parcours des neuf cases de la grille
        for x in range(3):
            for y in range(3):
                if tab.tableau[x][y] == " ":      # Cas où une case est vide
                    cases_libres.append((x, y))   # Ajout de ses coordonnées à la liste

        if len(cases_libres) == 0:                # Cas si la grille est pleine
            return None

        return random.choice(cases_libres)        # Une case libre est choisie au hasard



# ------- PARTIE C -------------------------------------------------------------------------
def partie():
    g = Grille()

    joueur_X = JoueurHumain()
    joueur_O = JoueurIA()

    joueur_actuel = "X"

    while True:
        print("\n=== TOUR DU JOUEUR", joueur_actuel, "===")
        g.afficher()

        # Choisir le joueur qui doit jouer
        if joueur_actuel == "X":
            joueur = joueur_X
        else:
            joueur = joueur_O

        # Demander son prochain coup
        coup = joueur.prochain_coup(g, joueur_actuel)

        if coup is None:
            print("Match nul !")
            break

        x, y = coup

        # Vérifier si le coup est valide
        if not g.jouer(x, y, joueur_actuel):
            print("Coup invalide, réessaie.")
            continue

        # Vérifier si le joueur a gagné
        if g.est_gagnant(joueur_actuel):
            g.afficher()
            print("Le joueur", joueur_actuel, "a gagné !")
            break

        # Vérifier si la grille est pleine
        if g.est_plein():
            g.afficher()
            print("Match nul !")
            break

        # Changer de joueur
        if joueur_actuel == "X":
            joueur_actuel = "O"
        else:
            joueur_actuel = "X"


# TESTS PARTIE A
"""
g = Grille()
g.jouer(0, 0, "X")
g.jouer(0, 1, "O")
g.jouer(1, 1, "X")
g.afficher()

# Test des coups invalides
print("======================")
g.jouer(0, 0, "O")  
g.jouer(3, 0, "O")  
g.afficher()

# Test de victoire
print("======================")
print("X gagnant : ", g.est_gagnant("X"))
g.afficher()

print("=======================")
g.jouer(2, 2, "X")
print("X gagnant : ", g.est_gagnant("X"))
g.afficher()

# Test de la grille pleine
print("======================")
print("Grille pleine :", g.est_plein())
g.afficher()

"""



# TESTS PARTIE B
"""
g = Grille()
humain = JoueurHumain()
ia = JoueurIA()

# Test du joueur humain
coup = humain.prochain_coup(g, "X")
x, y = coup
g.jouer(x, y, "X")

# Test du joueur IA
coup = ia.prochain_coup(g, "O")

if coup is not None:
    x, y = coup
    g.jouer(x, y, "O")

# Affichage du résultat
g.afficher()

"""


# TEST PARTIE C
partie()

