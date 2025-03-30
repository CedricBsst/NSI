# Exercice type BAC - Les graphes
**Cette exercice porte sur les structures de données FILE et PILE, les graphes et les algorithmes de parcours.**
## Partie A
Une agence de voyage organise différentes excursions dans un région de France et propose la visite de certaines villes. Ces excursions peuvent être visualisées sur le graphe ci-dessous : les sommets désignent les villes, les arêtes représentent les routes pouvant être empruntées pour relier deux villes et les poids des arêtes représentent des distances, exprimées en kilomètre.

![graphe pondere](./media/graphe%20pondere.png)

1. Déterminer le plus court chemin allant du sommet Mp au sommet Np et préciser la longueur, en kilomètre de ce chemin. Aucune justification n'est attendue.

On souhaite toujours se rendre du sommet Mp au sommet Nc mais en visitant le minimum de villes.
2. Déterminer les deux chemins possibles.

## Partie B
L'agence souhaite proposer un itinéraire permettant de visiter toutes les villes. On appelle G le graphe non pondéré ci-dessous.

![Graphe non pondere](./media/graphe%20non%20pondere.png)

On choisit d'implémenter un graphe par listes d'adjacence, à l'aide d'un dictionnaire en langage Python, dont :
- les clés sont les sommets du graphe ;
- la valeur associée à une clé est la liste des voisins de ce sommet clé.

Les sommets sont de type `str`.

3. Donner l'implémentation, en langage Python, du graphe de la figure 2. Le dictionnaire obtenu sera stocké dans une variable nommée `G`. Afin de faciliter la lisibilité, écrire chaque couple clé/valeur sur une nouvelle ligne.

On considère une file.
4. Indiquer la signification des lettres dans les acronymes LIFO et FIFO.
5. Indiquer l'acronyme utilisé pour désigner la structure de file.
Voici, en langage Python, les opérations pouvant être effectuées sut une telle file :
- `creerFile()` : renvoie une file vide ;
- `estVide(F)` : renvoie `True` si la file `F` est vide et `False` sinon ;
- `enfiler(F, e)` : ajoute l'élément `e` dans la file `F` ;
- `defiler(F)` : renvoie l'élément à la tête de la file `F` en le retirant de la file `F`.

On donne la fonction `parcours` ci-dessous. Cette fonction prend en paramètres un dictionnaire `graphe` représentant un graphe sous la forme de listes d'adjacence, et une chaîne de caractères `sommet` représentant un sommet du graphe.

```python
def parcours(graphe, sommet):
    f = creerFile()
    enfiler(F, sommet)
    visite = [sommet]
    while not estVide(f):
        s = defiler(f)
        for v in graphe[s]:
            if not (v in visite):
                visite.append(v)
                enfiler(f, v)
    return visite
```

6. Donner le résultat renvoyé par l'appel `parcours(G, 'Av')`.
7. Recopier, parmi les deux propositions ci-dessous, celle qui correspondent au type de parcours de graphe réalisé par la fonction `parcours` :
- **parcours A** : parcours en largeur ;
- **parcours B** : parcours en profondeur.

Dans la suite de l'exercice, la distance entre deux sommets désignera le nombre d'arêtes séparant ces deux sommets. Ainsi, la distance entre les sommets Mp et Nc du graphe de la figure 2 est 3.

8. En modifiant la fonction `parcours`, écrire une fonction `distance` ayant pour paramètres `graphe`, un dictionnaire représentant un graphe sous la forme de listes d'adjacence, et une chaîne de caractères `sommet` représentant un sommet du graphe. Cette fonction renvoie un dictionnaire tel que :
- les clés sont les sommets du graphe ;
- la valeur associée à une clé est la distance entre ce sommet clé et le sommet d'origine `sommet`.

9. Donner le résultat renvoyé par l'appel `distance(G, 'Av')`.

On considère une pile.

Voici, en langage Python, les opérations pouvant être effectuées sur une telle pile :
- `creerPile()` : renvoie une pile vide ;
- `estVide(P)` : renvoie `True` si la pile `P` est vide et `False` sinon ;
- `empiler(P, e)` : ajoute l'élément `e` au sommet de la pile `P` ;
- `depiler(P)` : renvoie le sommet de la pile `p` en le retirant de la pile `P`.

On donne, ci-dessous, le peudo-code d'un algorithme de parcours d'un graphe `G` à partir d'un sommet `s` :

```
créer une pile p
empiler s dans p
créer une liste visite contenant s
tant que p n'est pas vide
    x = depiler p
    si x n'est pas dans la liste visite
        ajouter x a la liste visite
        pour chaque voisin v de x
            empiler v dans p
        fin pour
    fin si
fin tant que
renvoyer visite
```
10. Traduire, dans le corps d'une fonction Python nommée `parcours2`, l'algorithme en pseudo-code donné précédemment. Cette fonction prendra pour paramètres `G`, un dictionnaire représentant un graphe sous la forme de listes d'adjacence, et une chaîne de caractères `s` représentant un sommet du graphe.
11. Donner un résultat possible renvoyé par l'appel `parcours2(G, 'av')`.