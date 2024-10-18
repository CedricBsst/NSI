def file_vide():
    '''Renvoie une file vide'''
    return []

def est_vide(file):
    '''Renvoie True si file est vide et False sinon'''
    return len(file) == 0

def enfiler(file, elt):
    '''enfile elt dans file'''
    file.append(elt)

def defiler(file):
    '''défile une valeur dans file
    CU : file ne doit pas être vide
    '''
    assert not est_vide(file)
    return file.pop(0)
