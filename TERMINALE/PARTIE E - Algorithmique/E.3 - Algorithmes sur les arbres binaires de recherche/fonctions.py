class arbre_binaire:
    def __init__(self, racine, sag, sad):
        self.racine = racine
        self.sag = sag
        self.sad = sad

    def get_racine(self):
        return self.racine
    
    def get_sag(self):
        return self.sag
    
    def get_sad(self):
        return self.sad
    
    def set_sad(self, droit):
        self.sad = droit
        
    def set_sag(self, gauche):
        self.sag = gauche

    def set_racine(self, racine):
        self.racine = racine

n10 = arbre_binaire(10, None, None)
n13 = arbre_binaire(13, None, None)
n17 = arbre_binaire(17, None, None)
n8 = arbre_binaire(8, None, n10)
n14 = arbre_binaire(14, n13, None)
n16 = arbre_binaire(16, None, n17)
n21 = arbre_binaire(21, None, None)
n12 = arbre_binaire(12, n8, n14)
n20 = arbre_binaire(20, n16, n21)
a = arbre_binaire(15, n12, n20)

def mini(arbre):
    if arbre.get_sag() == None:
        return arbre.get_racine()
    else:
        return mini(arbre.get_sag())

def maxi(arbre):
    if arbre.get_sad() == None:
        return arbre.get_racine()
    else:
        return maxi(arbre.get_sad())

def est_abr(arbre):
    if arbre  == None:
        return True
    else:
        if est_abr(arbre.get_sag()) and est_abr(arbre.get_sad()):
            if (arbre.get_sag() == None or arbre.get_racine() >= maxi(arbre.get_sag())) \
                  and (arbre.get_sad() == None or arbre.get_racine() <= mini(arbre.get_sad())):
                return True
            else:
                return False            
        else:
            return False

print(est_abr(a))

def recherche (v,arbre):
    if arbre == None :
        return False
    
    if v > arbre.get_racine():
       return recherche(v,arbre.get_sad())
    
    if v < arbre.get_racine() :
        return recherche(v,arbre.get_sag())
    
    if v == arbre.get_racine() :
        return True
    
def ajouter(v,arbre):
    if v > arbre.get_racine():
        if arbre.get_sad() == None:
            arbre.set_sad(arbre_binaire(v,None,None))
        else:
            ajouter(v,arbre.get_sad())
            
    else:
        if arbre.get_sag() == None:
            arbre.set_sag(arbre_binaire(v,None,None))
        else:
            ajouter(v,arbre.get_sag())
ajouter(100,a)
        
def supprimer(v, arbre):
    if arbre == None:
        return None
    if v < arbre.get_racine():
        arbre.set_sag(supprimer(v, arbre.get_sag()))
    elif v > arbre.get_racine():
        arbre.set_sad(supprimer(v, arbre.get_sad()))
    else:
        if arbre.get_sag() == None:
            return arbre.get_sad()
        elif arbre.get_sad() == None:
            return arbre.get_sag()
        else:
            arbre.set_racine(mini(arbre.get_sad()))
            arbre.set_sad(supprimer(mini(arbre.get_sad()), arbre.get_sad()))
    return arbre
    
supprimer(15,a)