# création d'un dictionnaire qui stocke les noms et les notes d'étudiants
d = {'Alice': 12, 'Bob': 15, 'Claire': 9.5}

def ajouter_etudiant(d, nom, note):
    d[nom] = note               # ajoute un étudiant avec sa note au dictionnaire
    
    # retourne le nom et la note de l'étudiant ajouté
    return f"Étudiant ajouté : {nom}, Note : {note}"    


def moyenne_classe(d):
    if not d:                   # vérifie si le dictionnaire est vide
        return "Aucun étudiant dans la classe."  
    
    somme = 0                   # somme initialisée à 0
    for note in d.values():     # parcourt les notes du dictionnaire
        somme += note           # calcule la somme des notes
    
    # retourne la moyenne de la classe en divisant la somme par le nombre d'étudiants
    return f"Moyenne de la classe : {somme / len(d)}"


def meilleur_etudiant(d):
    if not d:                  
        return "Aucun étudiant dans la classe."
    
    best = list(d.items())[0]   # initialise le meilleur étudiant avec le premier du dictionnaire
    for nom, note in d.items(): # parcourt les étudiants et leurs notes
        if note > best[1]:      # compare les notes pour trouver le meilleur étudiant
            best = (nom, note)  # remplace le meilleur étudiant si une note plus élevée est trouvée
    
    # retourne le nom et la note du meilleur étudiant
    return f"Meilleur étudiant : {best[0]}, Note : {best[1]}"


# affichage du dictionnaire
print(d)

# tests des fonctions
print(ajouter_etudiant(d, 'David', 14))
print(moyenne_classe(d))
print(meilleur_etudiant(d))
