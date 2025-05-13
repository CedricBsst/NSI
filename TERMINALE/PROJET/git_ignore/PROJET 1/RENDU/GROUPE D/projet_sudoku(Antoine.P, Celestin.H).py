# Une grille difficile
grille_difficile = [[9,0,0,1,0,0,0,0,5],[0,0,5,0,9,0,2,0,1],[8,0,0,0,4,0,0,0,0],[0,0,0,0,8,0,0,0,0],[0,0,0,7,0,0,0,0,0],[0,0,0,0,2,6,0,0,9],[2,0,0,3,0,0,0,0,6],[0,0,0,2,0,0,9,0,0],[0,0,1,9,0,4,5,7,0]]
# Une grille facile
grille_facile = [[0,0,0,4,0,0,0,9,2],[0,0,1,0,5,9,0,8,0],[0,0,0,6,0,7,0,0,0],[0,3,0,0,0,0,6,7,0],[0,0,6,8,0,4,5,0,0],[0,9,4,0,0,0,0,1,0],[0,0,0,1,0,2,0,0,0],[0,5,0,9,8,0,3,0,0],[2,1,0,0,0,5,0,0,0]]
# La grille vide
grille_vide = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]

def affichage(grille):
    for i in range(9):
        if i % 3 == 0:
            print("")
        print("|", end="")
        for j in range(9):
            if grille[i][j] == 0:
                print(".", end="")
            else:
                print(grille[i][j], end="")
            if j % 3 == 2:
                print("| |", end="")
            else:
                print("|", end="")
        print("")

def saisir_valeur(grille, valeur, numero_ligne, numero_colonne):
    if valeur < 1 or valeur > 9:
        print("Erreur: La valeur doit être entre 1 et 9.")
    elif numero_ligne < 0 or numero_ligne > 8:
        print("Erreur: Le numéro de ligne doit être entre 0 et 8.")
    elif numero_colonne < 0 or numero_colonne > 8:
        print("Erreur: Le numéro de colonne doit être entre 0 et 8.")
    else:
        if grille[numero_ligne][numero_colonne] == 0:
            grille[numero_ligne][numero_colonne] = valeur
        else:
            print("Impossible, car il y a déja une valeur.")



def ligne_correct(grille, numero_ligne):
    verif_ligne = []
    for comptage in grille[numero_ligne]:
        if comptage != 0:
            if comptage in verif_ligne:
                return False
            verif_ligne.append(comptage)
    return True


def colonne_correct(grille, numero_colonne):
    verif_colonne = []
    for comptage in range(9):
            valeur = grille[comptage][numero_colonne]
            if valeur != 0:
                if valeur in verif_colonne:
                    return False
                verif_colonne.append(valeur)
    return True


def block_correct(grille, col_premiere_case, ligne_premiere_case):
    verif_block = []
    for i in range(3):
        for j in range(3):
            valeur = grille[ligne_premiere_case + i][col_premiere_case + j]
            if valeur != 0:
                if valeur in verif_block:
                    return False
                verif_block.append(valeur)
    return True



def est_correct(grille):
    for i in range(9):
        if not ligne_correct(grille, i):
            print(f"Ligne {i} incorrecte")
            return False


    for i in range(9):
        if not colonne_correct(grille, i):
            print(f"Colonne {i} incorrecte")
            return False


    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            if not block_correct(grille, i, j):
                print(f"Bloc ({i}, {j}) incorrect")
                return False
    return True



def menu():
    choix = -1
    while choix != 4:
        try:
            choix = int(input("1 = afficher la grille\n2 = ajouter une valeur\n3 = vérifier la grille\n4 = fermer le programme\n"))
            if choix > 4 or choix < 1:
                print('il faut choisir un nombre entre 1 et 4')
            if choix == 1:
                affichage(grille_facile)
            elif choix == 2:
                try:
                    valeur = int(input("Quelle est la valeur entre 1 et 9 ? "))
                    numero_ligne = int(input("Quelle est la ligne entre 0 et 8 ? "))
                    numero_colonne = int(input("Quelle est la colonne entre 0 et 8 ? "))
                    saisir_valeur(grille_facile, valeur, numero_ligne, numero_colonne)
                except ValueError:
                    print("Erreur: Vous devez entrer des nombres entiers pour la valeur, la ligne et la colonne.")
            elif choix == 3:
                if est_correct(grille_facile):
                    print("La grille est valide.")
                else:
                    print("La grille contient des erreurs.")
                    grille_facile[numero_ligne][numero_colonne] = 0
            elif choix == 4:
                print("Fin du programme")
        except ValueError:
            print("Erreur: Vous devez entrer un nombre entier pour le choix du menu.")


menu()



