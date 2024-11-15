def tri_insertion(liste):
    '''tri de la liste en utilisant le tri par insertion
    :param: liste (list<int>)
    :return: (list<int>) liste triée par ordre croissant
    '''
    for i in range(1, len(liste)):
        # Sauvegarder la valeur à insérer
        valeur_a_inserer = liste[i]
        # Déplacer les éléments de la partie triée de la liste qui sont plus grands que valeur_a_inserer
        j = i - 1
        while j >= 0 and liste[j] > valeur_a_inserer:
            liste[j + 1] = liste[j]
            j -= 1
        # Insérer la valeur à sa position correcte
        liste[j + 1] = valeur_a_inserer
    return liste
