# Créé par vanec, le 29/09/2024 en Python 3.7

# Grilles de test
grille_difficile = [[9,0,0,1,0,0,0,0,5],[0,0,5,0,9,0,2,0,1],[8,0,0,0,4,0,0,0,0],
                    [0,0,0,0,8,0,0,0,0],[0,0,0,7,0,0,0,0,0],[0,0,0,0,2,6,0,0,9],
                    [2,0,0,3,0,0,0,0,6],[0,0,0,2,0,0,9,0,0],[0,0,1,9,0,4,5,7,0]]
grille_facile = [[0,0,0,4,0,0,0,9,2],[0,0,1,0,5,9,0,8,0],[0,0,0,6,0,7,0,0,0],
                 [0,3,0,0,0,0,6,7,0],[0,0,6,8,0,4,5,0,0],[0,9,4,0,0,0,0,1,0],
                 [0,0,0,1,0,2,0,0,0],[0,5,0,9,8,0,3,0,0],[2,1,0,0,0,5,0,0,0]]
grille_vide = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]

# Fonction pour afficher la grille
def affichage(grille):
    for i in range(9):
        if i % 3 == 0:
            print("###################")
        else:
            print("#-+-+-+-#-+-+-+-#-+-+-+-#")
        print("#", end="")
        for j in range(9):
            print(grille[i][j] if grille[i][j] != 0 else ".", end="")
            if j % 3 == 2:
                print("#", end="")
            else:
                print("|", end="")
        print("")
    print("###################")

# Saisir une valeur dans la grille avec vérification
def saisir_valeur(grille, valeur, ligne, colonne):
    if 1 <= valeur <= 9 and 0 <= ligne <= 8 and 0 <= colonne <= 8:
        if valeur in grille[ligne]:
            print("Erreur : La valeur existe déjà dans cette ligne.")
        elif valeur in [grille[i][colonne] for i in range(9)]:
            print("Erreur : La valeur existe déjà dans cette colonne.")
        else:
            bloc_ligne = ligne // 3 * 3
            bloc_colonne = colonne // 3 * 3
            if valeur in [grille[i][j] for i in range(bloc_ligne, bloc_ligne + 3)
                                          for j in range(bloc_colonne, bloc_colonne + 3)]:
                print("Erreur : La valeur existe déjà dans ce bloc.")
            else:
                grille[ligne][colonne] = valeur
    else:
        print("Erreur : Veuillez entrer une valeur valide (1-9) et une position correcte.")

# Vérifier si une ligne est correcte
def ligne_correct(grille, ligne):
    valeurs = [val for val in grille[ligne] if val != 0]
    return len(valeurs) == len(set(valeurs))

# Vérifier si une colonne est correcte
def colonne_correct(grille, colonne):
    valeurs = [grille[i][colonne] for i in range(9) if grille[i][colonne] != 0]
    return len(valeurs) == len(set(valeurs))

# Vérifier si un bloc est correct
def bloc_correct(grille, ligne, colonne):
    bloc_ligne = ligne // 3 * 3
    bloc_colonne = colonne // 3 * 3
    valeurs = [grille[i][j] for i in range(bloc_ligne, bloc_ligne + 3)
                                      for j in range(bloc_colonne, bloc_colonne + 3) if grille[i][j] != 0]
    return len(valeurs) == len(set(valeurs))

# Vérifier si la grille est correcte
def grille_correct(grille):
    for i in range(9):
        if not ligne_correct(grille, i):
            return False
        if not colonne_correct(grille, i):
            return False
    for i in range(3):
        for j in range(3):
            if not bloc_correct(grille, i * 3, j * 3):
                return False
    return True

# Programme principal
def main():
    grille = grille_vide
    while True:
        affichage(grille)
        print("1. Saisir une valeur")
        print("2. Vérifier la grille")
        print("3. Quitter")
        choix = input("Choix : ")
        if choix == "1":
            valeur = int(input("Valeur (1-9) : "))
            ligne = int(input("Ligne (0-8) : "))
            colonne = int(input("Colonne (0-8) : "))
            saisir_valeur(grille, valeur, ligne, colonne)
        elif choix == "2":
            if grille_correct(grille):
                print("La grille est correcte.")
            else:
                print("La grille n'est pas correcte.")
        elif choix == "3":
            break
        else:
            print("Erreur : Choix non valide.")

if __name__ == "__main__":
    main()