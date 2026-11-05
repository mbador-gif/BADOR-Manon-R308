# -------------- PARTIE A -------------------------------------------------------------------------

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


# -------------- PARTIE B -------------------------------------------------------------------------

class Bibliotheque:

    # Constructeur de la bibliothèque
    def __init__(self):

        # Dictionnaire contenant les livres
        # La clé est le titre et la valeur est un objet Livre
        self.livres = {}

        # Dictionnaire contenant les utilisateurs
        # La clé est le nom et la valeur est un objet Utilisateur
        self.utilisateurs = {}

    # Ajouter un livre dans la bibliothèque
    def ajouter_livre(self, livre):

        # Vérifie si le livre existe déjà
        if livre.titre in self.livres:
            print("Ce livre existe déjà.")
            return False

        # Ajoute le livre dans le dictionnaire
        self.livres[livre.titre] = livre
        print("Livre ajouté avec succès.")
        return True

    # Ajouter un utilisateur dans la bibliothèque
    def ajouter_utilisateur(self, utilisateur):

        # Vérifie si l'utilisateur existe déjà
        if utilisateur.nom in self.utilisateurs:
            print("Cet utilisateur existe déjà.")
            return False

        # Ajoute l'utilisateur au dictionnaire
        self.utilisateurs[utilisateur.nom] = utilisateur
        print("Utilisateur ajouté avec succès.")
        return True

    # Permet à un utilisateur d'emprunter un livre
    def emprunter(self, nom, titre):

        # Vérifie si l'utilisateur existe
        if nom not in self.utilisateurs:
            print("Utilisateur inconnu.")
            return False

        # Vérifie si le livre existe
        if titre not in self.livres:
            print("Livre inconnu.")
            return False

        # Récupère l'utilisateur et le livre
        utilisateur = self.utilisateurs[nom]
        livre = self.livres[titre]

        # Appelle la méthode de la classe Utilisateur
        return utilisateur.emprunter_livre(livre)

    # Permet à un utilisateur de rendre un livre
    def rendre(self, nom, titre):

        # Vérifie si l'utilisateur existe
        if nom not in self.utilisateurs:
            print("Utilisateur inconnu.")
            return False

        # Vérifie si le livre existe
        if titre not in self.livres:
            print("Livre inconnu.")
            return False

        # Récupère l'utilisateur et le livre
        utilisateur = self.utilisateurs[nom]
        livre = self.livres[titre]

        # Appelle la méthode pour rendre le livre
        return utilisateur.rendre_livre(livre)

    # Affiche tous les livres de la bibliothèque
    def afficher_livres(self):

        # Vérifie si la bibliothèque est vide
        if not self.livres:
            print("Aucun livre dans la bibliothèque.")
            return

        print("Liste des livres :")

        # Parcourt tous les livres du dictionnaire
        for livre in self.livres.values():

            # Utilise la méthode afficher de Livre
            livre.afficher()



# Tests de la Partie A
"""
l = Livre("1984", "Orwell", 1949)
print(l.emprunter("Anna"))
print(l.emprunter("Léo"))
print(l.rendre())

"""


# Tests de la Partie B
"""
biblio = Bibliotheque()
livre = Livre("1984", "Orwell", 1949)
ana = Utilisateur("Ana")
leo = Utilisateur("Léo")

# Ajout du livre et des utilisateurs
biblio.ajouter_livre(livre)
biblio.ajouter_utilisateur(ana)
biblio.ajouter_utilisateur(leo)

# Nom inconnu
print("\n--- Test nom inconnu ---")
biblio.emprunter("Paul", "1984")

# Titre inconnu
print("\n--- Test titre inconnu ---")
biblio.emprunter("Ana", "Harry Potter")

# Livre déjà emprunté
print("\n--- Test livre déjà emprunté ---")
biblio.emprunter("Ana", "1984")
biblio.emprunter("Léo", "1984")

"""

