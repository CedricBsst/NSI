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

def saisir_valeur(grille):
### sert a demander au joueur de rentrer une valeur
    try:
        numero_ligne = int(input("Entrez le numéro de ligne (1-9) : ")) - 1
        numero_colonne = int(input("Entrez le numéro de colonne (1-9) : ")) - 1
        valeur = int(input("Entrez la valeur (1-9) : "))

        if 0 <= numero_ligne <= 8 and 0 <= numero_colonne <= 8 and 1 <= valeur <= 9:
            if grille[numero_ligne][numero_colonne] == 0:
                grille[numero_ligne][numero_colonne] = valeur
            else:
                print("La case est déjà remplie, idiot !")
        else:
            print("Coordonnées ou valeur incorrecte, suis les instructions, ma parole !")
    except ValueError:
        print("Veuillez entrer des chiffres valides")
    return grille


def ligne_correct(grille, numero_ligne):
### sert a vérifié si le numéro rentré n'est pas déjà dans la ligne
    for valeur in grille[numero_ligne] :
        if valeur in grille[numero_ligne] :
            print( "pas possible")
        else :
            print ("c'est bon")


def colonne_correct(grille, numero_colonne):
### sert a vérifier si le numéro rentré n'est pas déjà dans la colonne
   ### if valeur ###différent de
   l=[]
   for i in range(9) :
            if grille[i][numero_colonne] in l :
                return False
            else :
                l.append(grille[i][numero_colonne])
            return True

def block_correct(grille, col_premiere_case, ligne_premiere_case):
### sert a vérifier si le numéro rentré n'est pas déjà dans le block
    l = []
    for j in range(3):
        for i in range(3):
            if grille[i+ligne_premiere_case][j+col_premiere_case] in l:
                return False
            else :
                l.append(grille[i+ligne_premiere_case][j+col_premiere_case])
    return True

def est_correct(grille):
### sert a vérifié si la grille est correct
    for i in range(9):
        if ligne_correct(grille, i):
            continue
        else:
            print(f"Ligne {i+1} incorrecte.") ### Je viens d'apprendre ça, le "f" est important pour remplacer les variables par leur valeur.
            return False                                                                            ###ex :
                                                                                                    ###nom = "Brieuc"
    for i in range(9):                                                                              ###print(f"Moi ?! Tu parles au saint-{nom} ?!")
        if colonne_correct(grille, i):                                                              ###
            continue                                                                                ###Moi ?! Tu parles au saint-Brieuc ?!
        else:
            print(f"Colonne {i+1} incorrecte.")
            return False

    for ligne_premiere_case in [0, 3, 6]:
        for col_premiere_case in [0, 3, 6]:
            if block_correct(grille, col_premiere_case, ligne_premiere_case):
                continue
            else:
                print(f"Bloc avec coin supérieur gauche ({ligne_premiere_case+1}, {col_premiere_case+1}) incorrect.")
                return False

    print("La grille est correcte.")
    return True

def menu() :
    grille_type = input("Choisissez une grille : grille_vide, grille_facile ou grille_difficile ? ").strip().lower()

    if grille_type == "grille_vide":
        grille = grille_vide
    elif grille_type == "grille_facile":
        grille = grille_facile
    elif grille_type == "grille_difficile":
        grille = grille_difficile
    else:
        print("Choix de grille invalide.")
        return

    while True:
        choix = input("Tapez 1 pour saisir une valeur, tapez 2 pour vérifier, tapez 3 pour afficher la grille, tapez 4 pour quitter : ")

        if choix == '1':
            grille = saisir_valeur(grille)
        elif choix == '2':
            if est_correct(grille):
                print("La solution est correcte !")
            else:
                print("La solution est incorrecte.")
        elif choix == '3':
            affichage(grille)
        elif choix == '4':
            print("Au revoir !")
            break
        else:
            print("Choix invalide, veuillez réessayer.")
menu()