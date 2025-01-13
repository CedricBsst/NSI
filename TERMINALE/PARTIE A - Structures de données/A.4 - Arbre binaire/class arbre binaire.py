class arbre_binaire:
    def __init__(self, valeur, sag, sad):
        self.racine = valeur
        self.gauche = sag
        self.droit = sad
    
    def get_racine(self):
        return self.racine
    
    def get_sag(self):
        return self.gauche
    
    def get_sad(self):
        return self.droit
