def tri_selection(liste):
    '''tri de la liste en utilisant le tri par sélection
    :param: liste (list<int>)
    :return: (list<int>) liste triée par ordre croissant
    '''
    for i in range(len(liste)):
        # Trouver l'indice de la valeur minimale dans la sous-liste non triée
        indice_min = i
        for j in range(i + 1, len(liste)):
            if liste[j] < liste[indice_min]:
                indice_min = j
        # Échanger la valeur minimale trouvée avec le premier élément de la sous-liste non triée
        liste[i], liste[indice_min] = liste[indice_min], liste[i]
    return liste
