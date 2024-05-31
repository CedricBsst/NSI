#  Fiche d'exercices - **Chapitre F.1 - Construction de programme**

## Exercice 1
Dans la console, tester les instructions et compléter le tableau suivant :
|Instruction|Résultat obtenu|Opération réalisée|
|-|-|-|
|```30 + 3```||
|```8 - 7```||
|```5 * 6```||
|```16 / 3```||
|```16 // 3```||
|```16 % 3```||
|```'He'+"llo"```||

## Exercice 2
1. Dans la console, taper l'instruction suivante
```python
type(0)
```
- ```type``` est une fonction déterminer ce qu'elle permet d'obtenir.
- Quel type de données en python permet donc de représenter un entier ?
2. Dans la console, utiliser la fonction ```type``` pour compléter le tableau suivant :

|valeur|Type python|Type de valeur représentée|
|-|-|-|
|```5```|||
|```5.3```|||
|```1.0```|||
|```True```|||
|```"Bonjour```|||

## Exercice 3
Dans la console python, tester les instructions et compléter le tableau suivant :
|Instruction|Résultat obtenu|Type du résultat|
|-|-|-|
|```9 + 5```|||
|```10 - 5```|||
|```12 * 15```|||
|```12 / 6```|||
|```65 % 4```|||
|```12.5 / 5.5```|||
|```4 < 5```|||
|```2 * 0.5```|||
|```10 // 2```|||
|```5 - 4.32```|||
|```25 <= 21```|||

## Exercice 4
Sans aide de python, determiner le type de chacune des opérations suivantes : 
|Instruction|Type du résultat|
|-|-|
|```1 + 1```||
|```1.0 + 1```||
|```3 == 4```||
|```‘Bonjour’ + ‘Monsieur’```||
|```1.0 – 1```||
|```1 * 5```||
|```1.0 * 5```||
|```5 – 5```||
|```5 ** 5```||
|```10 / 2```||
|```10 // 2```||
|```10 % 2```||

## Exercice 5
Sans l'aide de python, pour chacune des expressions suivantes, donner le résultat obtenu et son type.
- ```5 + 5.0```
- ```1 + 3```
- ```"Bonjour" + " le monde"```
- ```int("4" + "5")```
- ```"Le résultat est " + float(4 +int("5" + "0")) + "."```
- ```5 < 4```
- ```4 < 5```

## Exercice 6
Sans l'aide de python, determiner la valeur de la variable ```c``` à la fin de l'exécution du programme :
1. 
```python
a = 7
b = 10
c = a + b
```

2. 
```python
a = 0
a = a + 1
a = a + 2
c = a
```

3. 
```python
a = 4
b = 5
a = a + b
c = a + a
c = c + 5
```

4. 
```python
a1 = 1
a2 = 2
a3 = 3
somme = a1 + a2 + a3
c = "Le resultat est " + str(somme) + "."
```
## Exercice 7
Analyser les programmes suivants, que font-il ?

1. 
```python
a = int(input("Valeur 1"))
b = int(input("Valeur 2"))
c = a + b
print(c)
```

2. 
```python
valeur_1 = int(input("Quelle est la première valeur ?"))
valeur_2 = int(input("Quelle est la seconde valeur ?"))
plus_grand = valeur_1 > valeur_2
print(plus_grand)
```

## Exercice 8
Le programme suivant permet à l'utilisateur de connaître son age à partir de son année de naissance et de l'année actuelle. Compléter et tester le programme :
```python 
annee_actuelle = int(input("En quelle année sommes nous ?"))
annee_naissance = ...
age = ...
print("votre age est :", age)
```

## Exercice 9
Ecrire un programme qui demande la longueur et la largeur d'un rectangle et qui renvoie l'aire de celui-ci.
>**Rappel :**
>
>$aire = longueur \times largeur$

Tester votre programme.

## Exercice 10
On considère le programme suivant : 
```python
a = 0
b = a + 1
c = a + 2
print(a < c and c > b)
```

1. Qu'afiche le programme ?
2. A quoi sert l'opérateur ```and``` ?

On considère le programme suivant : 
```python
a = 0
b = a + 1
c = a + 2
print(a > c or c > b)
```
1. Qu'affiche le programme ?
2. A quoi sert l'opérateur ```or``` ?