# Une grille difficile
grille_difficile = [[9,0,0,1,0,0,0,0,5],[0,0,5,0,9,0,2,0,1],[8,0,0,0,4,0,0,0,0],[0,0,0,0,8,0,0,0,0],[0,0,0,7,0,0,0,0,0],[0,0,0,0,2,6,0,0,9],[2,0,0,3,0,0,0,0,6],[0,0,0,2,0,0,9,0,0],[0,0,1,9,0,4,5,7,0]]
# Une grille facile
grille_facile = [[0,0,0,4,0,0,0,9,2],[0,0,1,0,5,9,0,8,0],[0,0,0,6,0,7,0,0,0],[0,3,0,0,0,0,6,7,0],[0,0,6,8,0,4,5,0,0],[0,9,4,0,0,0,0,1,0],[0,0,0,1,0,2,0,0,0],[0,5,0,9,8,0,3,0,0],[2,1,0,0,0,5,0,0,0]]
# La grille vide
grille_vide = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]

def affichage(grille):
    for i in range(9):
        if i % 3 == 0:
            print("+-------+-------+-------+")
        print("|", end=" ")
        for j in range(9):
            print(grille[i][j], end=" ")
            if (j + 1) % 3 == 0:
                print("|", end=" ")
        print()
    print("+-------+-------+-------+")


def saisir_valeur(grille, valeur, numero_ligne, numero_colonne):
    if grille[numero_ligne][numero_colonne] != 0:
        print(f"La case ({numero_ligne + 1}, {numero_colonne + 1}) est déjà remplie.")
        return False

        if valeur in grille[numero_ligne]:
            print(f"La valeur {valeur} est déjà présente dans la ligne {numero_ligne + 1}.")
        return False

    for i in range(9):
        if grille[i][numero_colonne] == valeur:
            print(f"La valeur {valeur} est déjà présente dans la colonne {numero_colonne + 1}.")
            return False

    debut_ligne = (numero_ligne // 3) * 3
    debut_colonne = (numero_colonne // 3) * 3
    for i in range(3):
        for j in range(3):
            if grille[debut_ligne + i][debut_colonne + j] == valeur:
                print(
                    f"La valeur {valeur} est déjà présente dans la sous-grille 3x3 à partir de ({debut_ligne + 1}, {debut_colonne + 1}).")
                return False

    grille[numero_ligne][numero_colonne] = valeur
    return True

def menu():
    # Une grille difficile
    grille_difficile = [[9,0,0,1,0,0,0,0,5],[0,0,5,0,9,0,2,0,1],[8,0,0,0,4,0,0,0,0],[0,0,0,0,8,0,0,0,0],[0,0,0,7,0,0,0,0,0],[0,0,0,0,2,6,0,0,9],[2,0,0,3,0,0,0,0,6],[0,0,0,2,0,0,9,0,0],[0,0,1,9,0,4,5,7,0]]
    # Une grille facile
    grille_facile = [[0,0,0,4,0,0,0,9,2],[0,0,1,0,5,9,0,8,0],[0,0,0,6,0,7,0,0,0],[0,3,0,0,0,0,6,7,0],[0,0,6,8,0,4,5,0,0],[0,9,4,0,0,0,0,1,0],[0,0,0,1,0,2,0,0,0],[0,5,0,9,8,0,3,0,0],[2,1,0,0,0,5,0,0,0]]
    # La grille vide
    grille_vide = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]

    g = str(input("Quelle grille voulez-vous ? (facile, difficile ou vide)"))

    if g == "facile":
        affichage(grille_facile)
        c = int(input("Définisez un nombre de coups"))
        for p in range(c):
            valeur = int(input("Quelle valeur voulez-vous mettre (entre 1 et 9) ? "))
            numero_ligne = int(input("Dans quelle ligne voulez-vous le jouer (entre 0 et 8) ? "))
            numero_colonne = int(input("Dans quelle colonne voulez-vous jouer (entre 0 et 8) ? "))
            saisir_valeur(grille_facile, valeur, numero_ligne, numero_colonne)
            affichage(grille_facile)

    if g == "difficile":
        affichage(grille_difficile)
        c = int(input("Définisez un nombre de coups"))
        for p in range(c):
            valeur = int(input("Quelle valeur voulez-vous mettre (entre 1 et 9) ? "))
            numero_ligne = int(input("Dans quelle ligne voulez-vous le jouer (entre 0 et 8) ? "))
            numero_colonne = int(input("Dans quelle colonne voulez-vous jouer (entre 0 et 8) ? "))
            saisir_valeur(grille_difficile, valeur, numero_ligne, numero_colonne)
            affichage(grille_difficile)

    if g == "vide":
        affichage(grille_vide)
        c = int(input("Définisez un nombre de coups"))
        for p in range(c):
            valeur = int(input("Quelle valeur voulez-vous mettre (entre 1 et 9) ? "))
            numero_ligne = int(input("Dans quelle ligne voulez-vous le jouer (entre 0 et 8) ? "))
            numero_colonne = int(input("Dans quelle colonne voulez-vous jouer (entre 0 et 8) ? "))
            saisir_valeur(grille_vide, valeur, numero_ligne, numero_colonne)
            affichage(grille_vide)

menu()