def factorial(x):
    """
    Calcule le factoriel d'un nombre n sans utiliser la récursion.
    
    :param n: Un entier non négatif
    :return: Le factoriel de n
    """
    result = 1
    for i in range(1, x + 1):
        result = result * i
    return result

# Déterminez la complexité de cet algorithme.

def exists_greater_than_single_return(lst, x):
    """
    Détermine s'il existe un nombre plus grand que x dans une liste en utilisant un seul return.
    
    :param lst: Une liste de nombres
    :param x: Un nombre
    :return: True s'il existe un nombre plus grand que x dans la liste, sinon False
    """
    exists = False
    for num in lst:
        if num > x:
            exists = True
    return exists

# Déterminez la complexité de cet algorithme.

def exists_greater_than(lst, x):
    """
    Détermine s'il existe un nombre plus grand que x dans une liste.
    
    :param lst: Une liste de nombres
    :param x: Un nombre
    :return: True s'il existe un nombre plus grand que x dans la liste, sinon False
    """
    for num in lst:
        if num > x:
            return True
    return False

# Déterminez la complexité de cet algorithme.

def exists_greater_than_while(lst, x):
    """
    Détermine s'il existe un nombre plus grand que x dans une liste en utilisant une boucle while.
    
    :param lst: Une liste de nombres
    :param x: Un nombre
    :return: True s'il existe un nombre plus grand que x dans la liste, sinon False
    """
    i = 0
    exists = False
    while i < len(lst) and not exists:
        if lst[i] > x:
            exists = True
        i += 1
    return exists

# Donner la preuve que l'algorithme exists_greater_than_while s'arrête.




