def mini(liste):
    '''recherche de la plus petite valeur de liste
    :param:liste (list<int>)
    :return: (int) plus petite valeur de la liste
    :CU: liste ne doit pas être vide
    '''
    valeur_mini = liste[0]
    for i in range(1, len(liste)):
        if liste[i] < valeur_mini:
            valeur_mini = liste[i]
    return valeur_mini

def maxi(liste):
    '''recherche de la plus grande valeur de la liste
    :param: liste(list<int>)
    :return: (int) plus grande valeur de la liste
    :CU: liste ne doit pas être vide
    '''
    valeur_maxi = liste[0]
    for i in range(1, len(liste)):
        if liste[i] > valeur_maxi:
            valeur_maxi = liste[i]
    return valeur_maxi