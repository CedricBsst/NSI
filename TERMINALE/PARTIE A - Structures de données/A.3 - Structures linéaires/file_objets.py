class File:
    '''Implémentation d'une file avec une liste en POO
    '''
    def __init__(self):
        '''Constructeur de la classe'''
        self.valeurs = []
    
    def enfiler(self, elt):
        '''Enfile elt dans la liste'''
        self.valeurs.append(elt)
    
    def defiler(self):
        '''Défile une valeur de la liste
        CU : La file ne doit pas être vide
        '''
        assert not self.est_vide(), "Impossible de défiler une pile vide"
        return self.valeurs.pop(0)
    
    def est_vide(self):
        '''True si la file est vide False sinon'''
        return len(self.valeurs) > 0