class File:
    '''Implémentation d'une file avec une liste de taille fixe en POO
    '''
    # Dans certain langage, le type liste n'existe pas. On utilise des tableaux. 
    # La taille d'un tableau est fixe, modifier la taille d'un tableau est très coûteux en ressources.
    # On utilise donc un tableau pour résoudre ce problème.
    # En revanche, la file à une taille maximale.

    def __init__(self, taille_max):
        self.valeurs = [None] * taille_max
        self.prochain_enfile = 0
        self.prochain_defile = 0
        self.est_vide = True
        self.est_pleine = False
    
    def est_pleine(self):
        return self.est_pleine
    
    def est_vide(self):
        return self.est_vide
    
    def enfiler(self, elt):
        assert not self.est_pleine
        self.est_vide = False
        self.valeurs[self.prochain_enfile] = elt
        self.prochain_enfile = (self.prochain_enfile + 1) % len(self.valeurs)
        if self.prochain_defile == self.prochain_enfile:
            self.est_pleine = True

    def defiler(self, elt):
        assert not self.est_vide
        self.est_pleine = False
        r = self.valeurs[self.prochain_defile]
        self.prochain_defile = (self.prochain_defile + 1) % len(self.valeurs)
        if self.prochain_defile == self.prochain_enfile:
            self.est_pleine = True