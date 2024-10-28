def est_triee(liste):
    '''vérifie si liste est triée
    :param:liste(list)
    :return: (bool) True si la liste est triée et False sinon
    '''
    for i in range(1, len(liste)):
        if liste[i] < liste[i-1]:
            return False
    return True

def recherche_dichotomique(liste, valeur):
    ''' recherche de valeur dans une liste triée
    :param:liste(list)
    :param:valeur(int) valeur à rechercher
    :CU: liste doit être triée
    '''
    # Vérification des préconditions
    assert est_triee(liste), "La liste doit être triée"

    # Code de la fonction
    i_debut = 0
    i_fin = len(liste) - 1
    while i_debut <= i_fin:
        i_milieu = (i_debut + i_fin) // 2
        if liste[i_milieu] == valeur:
            return True
        elif liste[i_milieu] < valeur:
            i_debut = i_milieu + 1
        else:
            i_fin = i_milieu - 1
    return False