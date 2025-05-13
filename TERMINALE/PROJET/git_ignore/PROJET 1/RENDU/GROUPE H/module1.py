# Une grille difficile
grille_difficile = [[9,9,0,1,0,0,0,0,5],[9,0,5,0,9,0,2,0,1],[9,0,0,0,4,0,0,0,0],[0,0,0,0,8,0,0,0,0],[9,0,0,7,0,0,0,0,0],[0,0,0,0,2,6,0,0,9],[2,0,0,3,0,0,0,0,6],[0,0,0,2,0,0,9,0,0],[0,0,1,9,0,4,5,7,0]]
# Une grille facile
grille_facile = [[0,0,0,4,0,0,0,9,2],[0,0,1,0,5,9,0,8,0],[0,0,0,6,0,7,0,0,0],[0,3,0,0,0,0,6,7,0],[0,0,6,8,0,4,5,0,0],[0,9,4,0,0,0,0,1,0],[0,0,0,1,0,2,0,0,0],[0,5,0,9,8,0,3,0,0],[2,1,0,0,0,5,0,0,0]]
# La grille vide
grille_vide = [[1,2,3,4,4,5,6,7,8],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]

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
    grille[numero_ligne][numero_colonne]= valeur

def ligne_correct(grille, numero_ligne):
    liste_vide = []
    for i in range(9):
        if grille[numero_ligne][i] != 0 and grille[numero_ligne][i] in liste_vide:
            return False
        elif  grille[numero_ligne][i] != 0 and not grille[numero_ligne][i] in liste_vide:
            liste_vide.append(grille[numero_ligne][i])
    return True

def colonne_correct(grille, numero_colonne):
    liste_vide=[]
    for j in range(9):
        if grille [j][numero_colonne] !=0  and grille [j][numero_colonne] in liste_vide:
            return False
        elif grille [j][numero_colonne] !=0  and not grille [j][numero_colonne] in liste_vide:
            liste_vide.append(grille[numero_colonne][j])
    return True

def block_correct(grille, col_premiere_case, ligne_premiere_case):
    liste_vide=[]
    for i in range(3):
        for j in range(3):
            if grille[i+ligne_premiere_case][j+col_premiere_case] != 0 and grille[i+ligne_premiere_case][j+col_premiere_case] in liste_vide:
                return False
            elif  grille[i+ligne_premiere_case][j+col_premiere_case] != 0 and not grille[i+ligne_premiere_case][j+col_premiere_case] in liste_vide:
                liste_vide.append(grille[i+ligne_premiere_case][j+col_premiere_case])
    return True

def est_correct(grille):
    for i in range(9):
        if not ligne_correct(grille, i) or not colonne_correct(grille, i):
            return False

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            if not block_correct(grille, i, j):
                return False
    return True
def menu():
    print("Tapez 1 pour saisir la valeur")
    print("Tapez 2 pour vérifier le Sudoku")
    print("Tapez 3 pour quitter")
    flag=True
    while flag:
        choix = int(input("Choisissez une option: "))
        if choix in [1, 2, 3]:
            if choix==1:
                saisir_valeur(grille_difficile, int(input("saisir votre valeur ")), int(input ("numero ligne ")), int(input("numero colonne")))
            elif choix==2:
                est_correct(grille_difficile)
            elif choix==3:
                flag=False

        else:
            print("Option invalide. Réessayez.")
menu()



