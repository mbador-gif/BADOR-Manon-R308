
# Jeu du Morpion

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


# Tests Partie A
g = Grille()

g.jouer(0, 0, "X")
g.jouer(0, 1, "O")
g.jouer(1, 1, "X")

g.afficher()

g.jouer(0, 0, "O")
g.jouer(3, 0, "O")

g.afficher()

g.est_gagnant("X")

g.jouer(2, 2, "X")

g.afficher()

g.est_gagnant("X")
g.est_plein()



