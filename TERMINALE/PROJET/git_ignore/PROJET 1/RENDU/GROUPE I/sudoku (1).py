# Créé par cesaire, le 24/09/2024 en Python 3.7
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
    if grille[numero_ligne][numero_colonne] == 0:
        grille[numero_ligne][numero_colonne] = valeur
        return True
    else:
        print("Cette case est déjà remplie.")
        return False


def ligne_correct(grille, numero_ligne):
    valeurs = [x for x in grille[numero_ligne] if x != 0]
    for i in range(len(valeurs)):
        if valeurs[i] in valeurs[i+1:]:
            return False
    return True

def colonne_correct(grille, numero_colonne):
    valeurs = [grille[i][numero_colonne] for i in range(9) if grille[i][numero_colonne] != 0]
    for i in range(len(valeurs)):
        if valeurs[i] in valeurs[i+1:]:
            return False
    return True

def block_correct(grille, col_premiere_case, ligne_premiere_case):
    valeurs = []
    for i in range(3):
        for j in range(3):
            valeur = grille[ligne_premiere_case + i][col_premiere_case + j]
            if valeur != 0:
                valeurs.append(valeur)
    for i in range(len(valeurs)):
        if valeurs[i] in valeurs[i+1:]:
            return False
    return True


def est_correct(grille):
    for i in range(9):
        if not ligne_correct(grille, i) or not colonne_correct(grille, i):
            return False
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            if not block_correct(grille, j, i):
                return False
    return True


def menu():
    print("Menu Sudoku")
    print("1. Afficher grille facile")
    print("2. Afficher grille difficile")
    print("3. Saisir une valeur")
    print("4. Vérifier si la grille est correcte")
    print("5. Quitter")

    choix = int(input("Choisissez une option: "))

    if choix == 1:
        affichage(grille_facile)
    elif choix == 2:
        affichage(grille_difficile)
    elif choix == 3:
        ligne = int(input("Entrez le numéro de ligne (0-8): "))
        colonne = int(input("Entrez le numéro de colonne (0-8): "))
        valeur = int(input("Entrez la valeur (1-9): "))
        saisir_valeur(grille_facile, valeur, ligne, colonne)
    elif choix == 4:
        if est_correct(grille_facile):
            print("La grille est correcte.")
        else:
            print("La grille n'est pas correcte.")
    elif choix == 5:
        print("Merci d'avoir joué!")
        return False
    else:
        print("Choix invalide.")
    return True


menu()