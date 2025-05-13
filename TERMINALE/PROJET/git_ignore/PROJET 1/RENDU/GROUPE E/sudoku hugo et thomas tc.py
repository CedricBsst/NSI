# Une grille difficile
grille_difficile = [[9,0,0,1,0,0,0,0,5],[0,0,5,0,9,0,2,0,1],[8,0,0,0,4,0,0,0,0],[0,0,0,0,8,0,0,0,0],[0,0,0,7,0,0,0,0,0],[0,0,0,0,2,6,0,0,9],[2,0,0,3,0,0,0,0,6],[0,0,0,2,0,0,9,0,0],[0,0,1,9,0,4,5,7,0]]
# Une grille facile
grille_facile = [[0,0,0,4,0,0,0,9,2],[0,0,1,0,5,9,0,8,0],[0,0,0,6,0,7,0,0,0],[0,3,0,0,0,0,6,7,0],[0,0,6,8,0,4,5,0,0],[0,9,4,0,0,0,0,1,0],[0,0,0,1,0,2,0,0,0],[0,5,0,9,8,0,3,0,0],[2,1,0,0,0,5,0,0,0]]
# Grille vide
grille_vide = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]

def affichage(grille):
    print("\nGrille Sudoku :")
    for i in range(9):
        if i % 3 == 0:
            print("  +---------+---------+-------+")
        print(" |", end="")
        for j in range(9):
            if grille[i][j] == 0:
                print(" . ", end="")  
            else:
                print(f" {grille[i][j]} ", end="") # ici "f" sert a mettre des accolades pour changer les valeurs
            if j % 3 == 2:
                print("|", end="")
        print("")
    print("  +---------+---------+-------+\n")

def saisir_valeur(grille, valeur, numero_ligne, numero_colonne):
    if 1 <= valeur <= 9 and 0 <= numero_ligne < 9 and 0 <= numero_colonne < 9:
        grille[numero_ligne][numero_colonne] = valeur
    else:
        print("Valeur ou position incorrecte.")

def ligne_correct(grille, numero_ligne):
    ligne = [val for val in grille[numero_ligne] if val != 0]
    return len(ligne) == len(set(ligne))

def colonne_correct(grille, numero_colonne):
    colonne = [grille[i][numero_colonne] for i in range(9) if grille[i][numero_colonne] != 0]
    return len(colonne) == len(set(colonne))

def block_correct(grille, ligne_premiere_case, col_premiere_case):
    bloc = []
    for i in range(3):
        for j in range(3):
            valeur = grille[ligne_premiere_case + i][col_premiere_case + j]
            if valeur != 0:
                bloc.append(valeur)
    return len(bloc) == len(set(bloc))

def est_correct(grille):
    tout_est_bon = True

    for i in range(9):
        if not ligne_correct(grille, i):
            print(f"Problème dans la ligne {i + 1}")
            tout_est_bon = False

    for i in range(9):
        if not colonne_correct(grille, i):
            print(f"Problème dans la colonne {i + 1}")
            tout_est_bon = False

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            if not block_correct(grille, i, j):
                print(f"Problème dans le bloc 3x3 à la ligne {i + 1}, colonne {j + 1}") 
                tout_est_bon = False

    return tout_est_bon

def menu():
    print("Bienvenue au vérificateur de Sudoku.")
    
    print("Choisissez une grille :")
    print("1. Grille vide")
    print("2. Grille facile")
    print("3. Grille difficile")
    choix_grille = input("Votre choix (1, 2 ou 3) : ")

    if choix_grille == "2":
        grille = grille_facile
    elif choix_grille == "3":
        grille = grille_difficile
    else:
        grille = grille_vide

    while True:
        print("\n1. Afficher la grille")
        print("2. Ajouter une valeur")
        print("3. Vérifier la grille")
        print("4. Relancer le programme")
        choix = input("Faites un choix ")

        if choix == "1":
            affichage(grille)
        elif choix == "2":
            try:
                ligne = int(input("Numéro de ligne (0-8) "))
                colonne = int(input("Numéro de colonne (0-8) "))
                valeur = int(input("Valeur (1-9) "))
                saisir_valeur(grille, valeur, ligne, colonne)
            except ValueError:
                print("Vous n'avez pas entrer une bonne valeur")
        elif choix == "3":
            if est_correct(grille):
                print("LA GRILLE N'A PAS D'ERREUR")
            else:
                print("la grille a des erreurs")
        elif choix == "4":
            print("Relancement du programme")
            menu()  
        else:
            print("choix invalide")

menu()
