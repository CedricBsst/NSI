# Une grille difficile
grille_difficile = [[9,9,0,1,0,0,0,0,5],[0,0,5,0,9,0,2,0,1],[8,0,0,0,4,0,0,0,0],[0,0,0,0,8,0,0,0,0],[0,0,0,7,0,0,0,0,0],[0,0,0,0,2,6,0,0,9],[2,0,0,3,0,0,0,0,6],[0,0,0,2,0,0,9,0,0],[0,0,1,9,0,4,5,7,0]]
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
    grille[numero_ligne][numero_colonne]=valeur
    

def ligne_correct(grille, numero_ligne):
        for i in range(0,9):
            c=grille[numero_ligne].count(grille[numero_ligne][i])
            if c>1 and grille[numero_ligne][i]!=0 :
                return False
            else:
                return True
        
def colonne_correct(grille, numero_colonne):
    liste=[]
    for i in range(9):
        if grille[i][numero_colonne] in liste and grille[i][numero_colonne]!=0:
            return False
        else:
            liste.append(grille[i][numero_colonne])
    return True

def block_correct(grille, col_premiere_case, ligne_premiere_case):
    liste=[]
    for i in range(3):
        for j in range(3):
            if grille[ligne_premiere_case+i][col_premiere_case+j] in liste and grille[ligne_premiere_case+i][col_premiere_case+j]!=0:
                return False
            else:
                liste.append(grille[ligne_premiere_case+i][col_premiere_case+j])
    return True

def est_correct(grille):
    for i in range(9):
        if not ligne_correct(grille, i):
            return False
        if not colonne_correct(grille, i):
            return False
    for i in range(0,9,3):
        for j in range(0,9,3):
            if not block_correct(grille, i, j):
                return False
    return True

def menu():
   while True:
    print("taper 1 pour saisir une valeur")
    print("taper 2 pour verifier la grille:")
    print("taper 3 pour affiché la grille:")
    choix= int(input())
    if choix==1 :
        valeur=int(input("saisir la valeur:"))
        numero_de_colonne=int(input("numero_de_colonne:"))
        numero_de_ligne=int(input("numero_de_ligne:"))
        saisir_valeur(grille_facile,valeur,numero_de_ligne,numero_de_colonne)
    elif choix==2:
        print(est_correct(grille_facile))
    elif choix==3:
        print(affichage(grille_facile))
   
    
menu()