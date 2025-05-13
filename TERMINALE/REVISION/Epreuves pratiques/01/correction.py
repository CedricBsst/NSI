def recherche(tab,v):
    l=[]
    for i in range(len(tab)):
        if v==tab[i]:
            l.append(i)
    return l

def distance_carre(p1, p2):
    '''calcul et renvoie le carrée de la distance entre les deux points p1 et p2'''
    return (p2[0]-p1[0])**2 + (p2[1]-p1[1])**2

def point_le_plus_proche(dep, tab):
    ''' Renvoie les coordonnées du point dans tab ayant la plus courte distance avec le point dep.'''
    min_point = tab[0]
    min_dist = distance_carre(dep, min_point)
    for i in range(1, len(tab)):
        if distance_carre(dep, tab[i]) < min_dist:
            min_point = tab[i]
            min_dist = distance_carre(dep, tab[i])
    return min_point