# Créé par amine, le 30/09/2024 en Python 3.7
# Une grille difficile
grille_difficile = [[9,0,0,1,0,0,0,0,5],[0,0,5,0,9,0,2,0,1],[8,0,0,0,4,0,0,0,0],[0,0,0,0,8,0,0,0,0],[0,0,0,7,0,0,0,0,0],[0,0,0,0,2,6,0,0,9],[2,0,0,3,0,0,0,0,6],[0,0,0,2,0,0,9,0,0],[0,0,1,9,0,4,5,7,0]]
# Une grille facile
grille_facile = [[0,0,0,4,0,0,0,9,2],[0,0,1,0,5,9,0,8,0],[0,0,0,6,0,7,0,0,0],[0,3,0,0,0,0,6,7,0],[0,0,6,8,0,4,5,0,0],[0,9,4,0,0,0,0,1,0],[0,0,0,1,0,2,0,0,0],[0,5,0,9,8,0,3,0,0],[2,1,0,0,0,5,0,0,0]]
# La grille vide
grille_vide = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]

def affichage(grille):
    for i in range(9):
        if i%3 == 0:
            print("###################")
        else:
            print("#-+-+-#-+-+-#-+-+-#")
        print("#", end="")
        for j in range(9):
            print(grille[i][j], end="")
            if j%3 == 2:
                print("#",end="")
            else:
                print("|",end="")
        print("")
    print("###################")

def saisir_valeur(grille, valeur, numero_ligne, numero_colonne):
    grille[numero_ligne][numero_colonne] = valeur

def ligne_correct(grille, numero_ligne):
    ligne = [x for x in grille[numero_ligne] if x != 0]  # On ignore les 0
    return len(ligne) == len(set(ligne))  # Pas de doublon

def colonne_correct(grille, numero_colonne):
    colonne = [grille[i][numero_colonne] for i in range(9) if grille[i][numero_colonne] != 0]
    return len(colonne) == len(set(colonne))  # Pas de doublon

def block_correct(grille, col_premiere_case, ligne_premiere_case):
    bloc = []
    for i in range(3):
        for j in range(3):
            val = grille[ligne_premiere_case + i][col_premiere_case + j]
            if val != 0:
                bloc.append(val)
    return len(bloc) == len(set(bloc))  # Pas de doublon

def est_correct(grille):
    for i in range(9):
        if not ligne_correct(grille, i):
            return False
        if not colonne_correct(grille, i):
            return False
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            if not block_correct(grille, j, i):
                return False
    return True

def menu():
    # Sélectionner la grille (facile, difficile ou vide)
    choix = input("Choisir une grille (facile/difficile/vide) : ").lower()
    if choix == "facile":
        grille = grille_facile
    elif choix == "difficile":
        grille = grille_difficile
    else:
        grille = grille_vide

    affichage(grille)

    while True:
        print("\n1. Entrer une valeur")
        print("2. Vérifier si la grille est correcte")
        print("3. Afficher la grille")
        print("4. Quitter")

        choix = input("Votre choix : ")
        if choix == "1":
            ligne = int(input("Entrer la ligne (0-8) : "))
            colonne = int(input("Entrer la colonne (0-8) : "))
            valeur = int(input("Entrer la valeur (1-9) : "))
            saisir_valeur(grille, valeur, ligne, colonne)
        elif choix == "2":
            if est_correct(grille):
                print("La grille est correcte.")
            else:
                print("La grille n'est pas correcte.")
        elif choix == "3":
            affichage(grille)
        elif choix == "4":
            break

menu()
