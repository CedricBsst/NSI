# Correction
## PARTIE A
### Q.1 
Attribut
### Q.2
str
### Q.3
```python
ge = Region("Grand Est")
```
### Q.4
```python
def renvoie_premiere_couleur_disponible(self):
    '''
    Renvoie la première couleur du tableau des couleurs disponibles supposé non vide.
    : return (str)
    '''
    return self.tab_couleurs_disponibles[0]
```
### Q.5
```python
def renvoie_nb_voisines(self) :
    '''
    Renvoie le nombre de régions voisines.
    : return (int)
    '''
    return len(self.tab_voisines)
```
### Q.6

```python
def est_coloriee(self):
    '''
    Renvoie True si une couleur a été attribuée à cette région et False sinon.
    : return (bool)
    '''
    if self.couleur_attribuee == None:
        return False
    else:
        return True

    # return self.couleur_attribuee != None
```
### Q.7
```python
def retire_couleur(self, couleur):
    '''
    Retire couleur du tableau de couleurs disponibles de la région si elle est dans ce tableau. Ne fait rien sinon.
    : param couleur (str)
    : ne renvoie rien
    : effet de bord sur le tableau des couleurs disponibles
    '''
    if couleur in self.tab_couleur_disponible:
        self.tab_couleur_disponible.remove(couleur)
```
### Q.8
```python
def est_voisine(self, region):
    '''
    Renvoie True si la region passée en paramètre est une voisine et False sinon.
    : param region (Region)
    : return (bool)
    '''
    for i in self.tab_voisines:
        if i == region:
            return True
    return False
```
## PARTIE B 
### Q.9
```python
def renvoie_tab_regions_non_coloriees(self):
    '''
    Renvoie un tableau dont les éléments sont les régions du pays sans couleur attribuée.
    : return (list) tableau d’instances de la classe Region
    '''
    lst = []
    for i in self.tab_region:
        if not i.est_coloriee():
            lst.append(i)
    return lst
            
```
### Q.10
a)Cette méthode renvoie none dans le cas où toutes les regions sont coloriées

b)dans le cas où la méthode ne renvoie pas none la région renvoyé est la région non colorié qui possède le plus de voisines 


