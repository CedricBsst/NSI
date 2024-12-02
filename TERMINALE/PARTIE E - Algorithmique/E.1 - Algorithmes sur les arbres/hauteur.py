class ArbreBinaire():
    def __init__(self, sous_arbre_gauche, sous_arbre_droit):
        self.sous_arbre_gauche = sous_arbre_gauche
        self.sous_arbre_droit = sous_arbre_droit
    
    def get_sag(self):
        return self.sous_arbre_gauche
    
    def get_sad(self):
        return self.sous_arbre_droit

# Cet algorithme considère que l'arbre ne contenant qu'un noeud est de hauteur 1
def hauteur(arbre):
    if arbre == None: # Si l'arbre est vide, on renvoie 0 
        return 0
    else: 
        return 1 + max(hauteur(arbre.get_sag()), hauteur(arbre.get_sad()))


# Cet algorithme considère que l'arbre ne contenant qu'un noeud est de hauteur 0
def hauteur2(arbre):
    if arbre == None: # Si l'arbre est vide, on renvoie 0 
        return -1
    else: 
        return 1 + max(hauteur2(arbre.get_sag()), hauteur2(arbre.get_sad()))