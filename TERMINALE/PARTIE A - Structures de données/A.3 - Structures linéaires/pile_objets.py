class Pile:
    '''Implémentation d'une pile avec une liste en POO
    '''
    def __init__(self):
        '''Constructeur de la classe'''
        self.valeurs = []
    
    def empiler(self, elt):
        '''Empile elt dans la liste'''
        self.valeurs.append(elt)
    
    def depiler(self):
        '''Dépile une valeur de la liste
        CU : La pile ne doit pas être vide
        '''
        assert not self.est_vide(), "Impossible de dépiler une pile vide"
        return self.valeurs.pop()
    
    def est_vide(self):
        '''True si la pile est vide False sinon'''
        return len(self.valeurs) > 0