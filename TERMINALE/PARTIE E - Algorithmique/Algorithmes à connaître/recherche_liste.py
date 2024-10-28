def recherche1(liste, valeur):
    '''recherche de valeur dans liste
    :param: liste(list): liste de valeurs
    :param: valeur(any): valeur à rechercher
    :return: (bool) True si valeur est dans liste et False sinon
    '''
    for v in liste:
        if valeur == v:
            return True
    return False

def recherche2(liste, valeur):
    '''recherche de valeur dans liste
    :param: liste(list) liste de valeurs
    :param: valeur(any): valeur à rechercher
    :return: (int) indice de la première occurrence de valeur dans liste, -1 si valeur n'est pas dans liste
    '''
    for i in range(len(liste)):
        if valeur == liste[i]:
            return i
    return -1

def recherche3(liste, valeur):
    '''recherche de valeur dans liste
    :param: liste(list) liste de valeurs
    :param: valeur(any): valeur à rechercher
    :return: (list<int>) liste des indices de valeurs dans liste. La liste vide si valeur n'est pas dans liste
    '''
    liste_indices = []
    for i in range(len(liste)):
        if valeur == liste[i]:
            liste_indices.append(i)
    return liste_indices