# Chapitre B.4 - Les listes en compréhension

## Introduction
**Exercice 1**
1. Écrire un programme permettant de créer une liste `liste` de cent 0.
2. Écrire un programme permettant de créer une liste `liste` contenant les nombre entier naturel de 0 à 50.
3. On considère une liste `l` d'entiers. Écrire un programme permettant de créer une liste `liste` contenant les éléments positif de `l`.

Une liste en compréhension est une expression permettant de construire une liste à partir de tout autre type d’itérable (liste, tuple, chaîne de caractères …). Le résultat obtenu est toujours une liste. L’écriture d’une telle expression est plus compacte. Une liste en compréhension revêt la forme suivante : 

```python
ma_liste = [<expression> for <element> in <iterable>]
```

**Exemple : Une liste contenant les dix premiers entiers naturels**

<span class=caché> ma_liste = [i for i in range(10)]

## Boucles imbriquées
Il est également possible de combiner deux itérations dans une liste en compréhension. Cela permet de réaliser une itération sur chaque élément de la liste ou de l’itération de départ.

**Exemple :**
```python
liste = ["Bonjour", "tout", "le","monde"]
nouvelle_liste = [c for mot in liste for c in mot]


['B', 'o', 'n', 'j', 'o', 'u', 'r', 't', 'o', 'u', 't', 'l', 'e', 'm', 'o', 'n', 'd', 'e']
```
## Tableau de tableau
Il est possible de créer un tableau de tableau à l’aide des listes en compréhensions.

**Exemple : Un tableau de tableau de 5 par 5 ne contenant que des 0**

```python
ma_liste = [[0 for i in range(5)] for j in range(5)]


[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
```
## Conditions
Il est possible d'ajouter des conditions pour ne pas sélectionner tous les éléments :

**Exemple : La listes des entiers naturels impair inférieur à 20**
```python
ma_liste = [i for i in range(20) if i%2 == 1]


[1,3,5,7,9,11,13,15,17,19]
```

## Exercices 
**Exercice 2**
Pour chacun des tableaux suivants, indiquez quelles valeurs sont dans le tableau
1. monTab = [4*nb for nb in range(100)]
2. monTab = [3*nb for nb in range(100) if nb%2==0]
3. monTab = [lettre for lettre in ‘Abracadabra’]
4. monTab = [let for let in ‘Abracadabra’ if let.upper() != ‘A’]

    La méthode upper renvoie la chaîne de caractère passé en paramètre écrite en majuscule.
5. monTab = [ord(let) for let in ‘Abracadabra’]

    La fonction ord renvoie l’entier correspondant à la valeur en ASCII de la lettre passé en paramètre.

**Exercice 3**

Construire les listes suivantes en compréhensions :

1. Une liste contenant toutes les valeurs comprises entre 5 et 120
2. Une liste contenant tous les entiers divisibles par 10 plus petits que 100
3. Une liste de 10 listes contenant chacune 10 chaîne de caractère vide
4. Une liste comprenant toutes les lettres de la phrase : « Je suis un élève de première au lycée Léonard de Vinci » sans les espaces et toutes les lettres en majuscules.

