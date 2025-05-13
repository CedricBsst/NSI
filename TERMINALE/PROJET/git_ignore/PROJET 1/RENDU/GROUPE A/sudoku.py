# Une grille difficile
grille_difficile = [[9, 0, 0, 1, 0, 0, 0, 0, 5], [0, 0, 5, 0, 9, 0, 2, 0, 1], [8, 0, 0, 0, 4, 0, 0, 0, 0],
                    [0, 0, 0, 0, 8, 0, 0, 0, 0], [0, 0, 0, 7, 0, 0, 0, 0, 0], [0, 0, 0, 0, 2, 6, 0, 0, 9],
                    [2, 0, 0, 3, 0, 0, 0, 0, 6], [0, 0, 0, 2, 0, 0, 9, 0, 0], [0, 0, 1, 9, 0, 4, 5, 7, 0]]
# Une grille facile
grille_facile = [[0, 0, 0, 4, 0, 4, 0, 9, 2], [0, 0, 1, 0, 5, 9, 0, 8, 0], [0, 0, 0, 6, 0, 7, 0, 0, 0],
                 [0, 3, 0, 0, 0, 0, 6, 7, 0], [0, 0, 6, 8, 0, 4, 5, 0, 0], [0, 9, 4, 0, 0, 0, 0, 1, 0],
                 [0, 0, 0, 1, 0, 2, 0, 0, 0], [0, 5, 0, 9, 8, 0, 3, 0, 0], [2, 1, 0, 0, 0, 5, 0, 0, 0]]
# La grille vide
grille_vide = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]


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



def ligne_correct(grille, num_ligne, valeur):  # Angélina
    if valeur in grille[num_ligne]:
        print(f"{valeur} est déjà présente dans la ligne")
        return False

    else:
        return True


def colonne_correct(grille, num_colonne, valeur):  # Terrence
    # pour chaque élément dans la colonne
    for i in range(0, len(grille)):
        if grille[i][num_colonne] == valeur:
            print(f"{valeur} est déjà présente dans la colonne")
            return False

    return True


def localiser_block(numero):  # Terrence
    if numero <= 3:
        return 1

    elif 3 < numero <= 6:
        return 2

    else:
        return 3


def block_correct(grille, valeur, num_ligne, num_colonne):  # Terrence

    # on fait ligne block et colonne block pour savoir sur quel block l'utilisateur se place sur sa grille
    ligne_block = localiser_block(num_ligne)
    colonne_block = localiser_block(num_colonne)

    # d'ici on va aller début du block jusqu'à la fin pour vérifier si la valeur n'est pas dedans
    for i in range(3 * ligne_block - 3, 3 * ligne_block):
        for y in range(3 * colonne_block - 3, 3 * colonne_block):
            if grille[i][y] == valeur:
                print(f"{valeur} est déjà présent dans le block")
                return False

    return True


def est_correct(grille, num_colonne, num_ligne, valeur):  # Angélina
    if colonne_correct(grille, num_colonne-1, valeur) and ligne_correct(grille, num_ligne-1, valeur) and block_correct(grille, valeur, num_ligne, num_colonne) is True:
        return True
    else:
        return False


def demander_verifier_rep(grille, num_ligne, num_colonne, valeur): # Terrence
    while True:
        reponse = input("Voulez vous vérifier votre réponse ? oui/non :")

        if reponse.lower() == "oui":
            if est_correct(grille, num_colonne, num_ligne, valeur) is True:
                grille[num_ligne - 1][num_colonne - 1] = valeur
                affichage(grille)
                print("C'est possible, la valeur à été rentrer")
                break

            else:
                print("Donc il y a une erreur")
                break

        elif reponse.lower() == "non":
            grille[num_ligne - 1][num_colonne - 1] = valeur
            affichage(grille)
            break

        else:
            print("Rentrez oui ou non")


def saisir_valeur(grille):  # Angélina et Terrence

    while True:  # Angélina
        # vérifie les erreurs possiblement crée par l'utilisateur
        try:

            num_ligne = int(input("Choisir un numéro de ligne à partir de 1 : "))
            num_colonne = int(input("Choisir un numéro de colonne à partir de 1 : "))
            # vérifier que l'utilisateur ne dépasse pas la grille de 9*9
            if num_ligne > 9 or num_ligne < 1 or num_colonne > 9 or num_colonne < 1:
                print("Veuiller ne pas dépasser la grille")


            else:  # Terrence
                while True:
                    valeur = int(input("Choisir une valeur : "))
                    if valeur > 9 or valeur < 1:
                        print("Rentrer une valeur entre 1 et 9")

                    else:
                        # demander si l'utilisateur veut vérifier sa réponse
                        demander_verifier_rep(grille, num_ligne, num_colonne, valeur)
                        break

                break

        except ValueError:
            print("Veuillez rentrer une valeur correct")


def menu(grille):  # Angélina
    print("Vous êtes dans un correcteur de Sudoku")
    # tant que l'utilisateur veut jouer
    jouer = True
    while jouer is True:

        affichage(grille)
        # on lui demande de saisir une valeur
        saisir_valeur(grille)

        # pour savoir si il veut continuer
        while True:
            reponse = input("Voulez vous continuer ? : ")
            # si la réponse en minuscule est oui, on casse la boucle
            if reponse.lower() == "oui":
                break

            # sinon si elle vaut non on met "jouer" à False arrêtant la boucle principale et on casse cette boucle
            elif reponse.lower() == "non":
                jouer = False
                break

            else:
                print("Veuillez rentrer une réponse valide")


menu(grille_facile)

