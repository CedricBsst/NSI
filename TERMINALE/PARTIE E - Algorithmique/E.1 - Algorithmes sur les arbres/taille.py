class ArbreBinaire():
    def __init__(self, sous_arbre_gauche, sous_arbre_droit):
        self.sous_arbre_gauche = sous_arbre_gauche
        self.sous_arbre_droit = sous_arbre_droit
    
    def get_sag(self):
        return self.sous_arbre_gauche
    
    def get_sad(self):
        return self.sous_arbre_droit

def taille(arbre):
    if arbre == None: # Si l'arbre est vide, on renvoie 0 
        return 0
    else: 
        return 1 + taille(arbre.get_sag()) + taille(arbre.get_sad())
    