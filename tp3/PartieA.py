
class Livre:
    # Constructeur de la classe Livre
    def __init__(self, titre, auteur, annee):
        # On initialise les attributs du livre avec les valeurs passées en paramètres
        self.titre = titre
        self.auteur = auteur
        self.annee = annee

        # On initialise l'état du livre à disponible
        self.disponible = True

        # On initialise l'emprunteur à None, car le livre n'est pas encore emprunté
        self.emprunteur = None

    # Affiche les informations du livre
    def afficher(self):
        if self.disponible:         # Vérifie si le livre est disponible ou emprunté
            etat = "Disponible"
        else:
            etat = "Emprunté par " + self.emprunteur

        print(f"{self.titre} - {self.auteur} ({self.annee}) : {etat}")

    # Permet à un utilisateur d'emprunter le livre
    def emprunter(self, nom):
        # On vérifie si le livre est disponible
        if self.disponible:
            self.disponible = False     # Marque le livre comme emprunté
            self.emprunteur = nom       # Enregistre le nom de l'emprunteur
            return True

        # Si le livre est déjà emprunté, on refuse
        return False

    # Permet de rendre un livre
    def rendre(self):
        # On vérifie si le livre est emprunté
        if not self.disponible:
            self.disponible = True     # Marque le livre comme disponible
            self.emprunteur = None     # Réinitialise l'emprunteur à None
            return True

        # Cas si le livre était déjà disponible
        return False


class Utilisateur:
    # Constructeur de la classe Utilisateur
    def __init__(self, nom):
        self.nom = nom

        # Liste contenant les livres empruntés
        self.emprunts = []

    # Permet à l'utilisateur d'emprunter un livre
    def emprunter_livre(self, livre):
        # On utilise la méthode emprunter de Livre
        if livre.emprunter(self.nom):
            # On ajoute le livre à la liste des emprunts
            self.emprunts.append(livre)
            print("Emprunt effectué avec succès.")
            return True

        print("Ce livre est déjà emprunté.")
        return False

    # Permet à l'utilisateur de rendre un livre
    def rendre_livre(self, livre):
        # On vérifie que l'utilisateur possède ce livre
        if livre in self.emprunts:
            # On remet le livre comme disponible
            if livre.rendre():
                # On retire le livre de sa liste
                self.emprunts.remove(livre)
                print("Livre rendu avec succès.")
                return True

        print("Vous n'avez pas emprunté ce livre.")
        return False

    # Affiche tous les livres empruntés par l'utilisateur
    def afficher_emprunts(self):
        print(f"Livres empruntés par {self.nom} :")

        # Si la liste des emprunts est vide, on affiche un message
        if not self.emprunts:
            print("Aucun livre emprunté.")
        else:
            # On parcourt tous les livres empruntés
            for livre in self.emprunts:
                print(f"- {livre.titre}")


# Tests de la Partie A
l = Livre("1984", "Orwell", 1949)
print(l.emprunter("Anna"))
print(l.emprunter("Léo"))
print(l.rendre())