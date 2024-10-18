def pile_vide():
    '''Renvoie une pile vide'''
    return []

def est_vide(pile):
    '''Renvoie True si pile est vide et False sinon'''
    return len(pile) == 0

def empiler(pile, elt):
    '''empile elt dans pile'''
    pile.append(elt)

def depiler(pile):
    '''dépile une valeur dans pile
    CU : pile ne doit pas être vide
    '''
    assert not est_vide(pile)
    return pile.pop()
