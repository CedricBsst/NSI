# Fiche d'exercices - **Chapitre B.2 - Les dictionnaires**

## Exercice 1
1. Créer un dictionnaire contenant votre nom, votre prénom, votre age et votre classe.
2. En utilisant les valeurs du dictionnaires, écrire l'instruction permettant d'afficher dans la console la phrase suivante : 

"Bonjour je m'appelle PRENOM NOM, j'ai AGE ans et je suis en CLASSE"

## Exercice 2
Considérons le dictionnaire suivant :
```python 
mydict = {"device": "laptop", "constructeur": "acer", "ram": "8G", "processeur": "Intel core i5", "stockage": "500 G"}
```

1. Modifier la valeur correspondant à la clé "stockage", mettre la valeur "750 G".
2. Ajouter la paire clé-valeur : "Système d'exploitation": "WINDOWS 10".
3. Écrire trois fonctions suivantes
- La fonction prend un dictionnaire en paramètre et affiche l'ensemble des clés du dictionnaire
- La fonction prend un dictionnaire en paramètre et affiche l'ensemble des valeurs du dictionnaire
- La fonction prend un dictionnaire en paramètre et affiche l'ensemble des couples (clé, valeur) du dictionnaire.

## Exercice 3
On considère les trois dictionnaires Pythons qui regroupe la totalité du matériels informatiques:

```python
dicPC={"HP": 11 , "Acer": 7 , "Lenovo": 17 , "Del": 23}
dicPhone={"Samsung": 22 , "Iphone": 9 , "OnePlus": 13 }
dicTablette = {"Galaxy": 15 , "Other": 13}
```

Écrire un programme Python qui crée un nouveau dictionnaire contenant l’ensemble des couples clés-valeurs de chaque dictionnaire.

## Exercice 4
On considère le dictionnaire suivant dont les clés sont les noms des élèves et les valeurs des clés sont les moyennes générales obtenues en passant l'examen final:
```python
etudiants = {"etudiant_1" : 13 , "etudiant_2" : 17 , "etudiant_3" : 9 ,
 "etudiant_4" : 15 , "etudiant_5" : 8 , "etudiant_6" : 14 ,  "etudiant_7" : 16 , "etudiant_8" : 12 , "etudiant_9" : 13 ,  "etudiant_10" : 15 , "etudiant_11" : 14 , "etudiant_112" : 9 ,  "etudiant_13" : 10 , "etudiant_14" : 12 , "etudiant_15" : 13 ,  "etudiant_16" : 7 , "etudiant_17" : 12 , "etudiant_18" : 15 ,  "etudiant_19" : 9 , "etudiant_20" : 17 }
```
Ecrire un programme Python qui partitionne ce dictionnaire en deux sous dictionnaires:
1.	```etudiantAdmis``` dont les clés sont les étudiants admis et les valeurs des clés sont les moyennes obtenues (moyenne supérieures ou égales à 10 ).
2.	```etudiantNonAdmis``` dont les clés sont les étudiants non admis et les valeurs des clés sont les moyennes obtenues (moyenne inférieur ou égale à 10).

## Exercice 5
Écrire une fonction ```dico_occurence(c)``` Python qui prend une chaîne de de caractère en paramètre et qui renvoie un dictionnaire dans lequel les clés sont les lettres de la chaîne et les valeurs correspondent au nombre d’occurrence du caractère dans la chaîne.
Par exemple, ```dico_occurence("langages")``` doit renvoyer le dictionnaire ```{"l" : 1, "a": 2, "n" : 1, "g" : 2, "e" : 1, "s" : 1}```