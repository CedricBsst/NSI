class Pile:
    '''Implémentation d'une pile avec une liste de taille fixe en POO
    '''
    # Dans certain langage, le type liste n'existe pas. On utilise des tableaux. 
    # La taille d'un tableau est fixe, modifier la taille d'un tableau est très coûteux en ressources.
    # On utilise donc un tableau pour résoudre ce problème.
    # En revanche, la pile à une taille maximale.

    def __init__(self, taille_max):
        '''Constructeur de la classe'''
        self.valeurs = [None] * taille_max
        self.i_prochain_empile = 0

    def est_vide(self):
        '''Renvoie True si la pile est vide et False sinon'''
        return self.i_prochain_empile == 0
    
    def est_pleine(self):
        '''Renvoie True si la pile est pleine et False sinon'''
        return self.i_prochain_empile == len(self.valeurs)
    
    def empiler(self, elt):
        '''Empile elt dans la liste
        CU : La pile ne doit pas être pleine
        '''
        assert not self.est_pleine, "Impossible d'empiler une pile pleine"
        self.valeurs[self.i_prochain_empile] = elt
        self.i_prochain_empile = self.i_prochain_empile + 1

    def depiler(self):
        '''Dépile un élément de la pile
        CU : La pile ne doit pas être vide
        '''
        assert not self.est_vide, "Impossible de dépiler une pile vide"
        self.i_prochain_empile = self.i_prochain_empile - 1
        return self.valeurs[self.i_prochain_empile]
    