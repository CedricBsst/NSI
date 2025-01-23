# Chapitre B.3 - Requêtes de mise à jour
## I. Introduction
Dans cette leçon, on prendra pour exemple la table de données céée à l'aide des deux requêtes SQL suivantes :
```sql
CREATE TABLE Prof(num_prof INTEGER,
                  nom VARCHAR(64) NOT NULL,
                  salle VARCHAR(64),
                  PRIMARY KEY(num_prof)
                 );

CREATE TABLE Eleve (num_eleve INTEGER,
                    nom VARCHAR(64),
                    prenom VARCHAR(64),
                    id_pp INTEGER REFERENCES Prof(num_prof),
                    PRIMARY KEY(num_eleve)
                );
```
Le schéma relationnel de la table de données :
- <span class="caché">Prof(**num_prof**, nom, salle)</span>
- <span class="caché">Eleve(**num_eleve**, nom, prenom, #id_pp)</span>

## II. Insérer des données dans un table de données
Pour insérer des données dans une table, il existe deux méthodes :
```sql
INSERT INTO table VALUES (valeur1, valeur2, valeur3, ...);
```
```sql
INSERT INTO table (champ1, champ2, champ3,...) VALUES (valeur1, valeur2, valeur3,...);
```

**Exemple :**

Compléter les requêtes suivantes :

1.	Objectif de la requête 	: insérer dans la relation Prof le numéro 1 : Monsieur « Latouche » ayant pour salle « comédie ».

Requête SQL : …………………………………………………………………………………………………………………………………………………..

2.	Objectif de la requête : insérer l’élève « Léonie Gratin » ayant pour numéro 1 et pour professeur principal M. Latouche.

Requête SQL : …………………………………………………………………………………………………………………………………………………..

3.	Requête SQL : ```INSERT Eleve(num_eleve, nom) VALUES (1, ‘Ducobu’)``` ;

Objectif de la requête  : ….………………………………………………………………………………………………………………………………..

Problème rencontré : ……………………………………………………………………………………………………………………………………..

Modification proposée : …………………………………………………………………………………………………………………………………..

4.	Requête SQL : ```INSERT Eleve(num_eleve, prenom) VALUES (3, ‘Fatima’)``` ;

Objectif de la requête  : ….………………………………………………………………………………………………………………………………..

Problème rencontré : ……………………………………………………………………………………………………………………………………..

Modification proposée : …………………………………………………………………………………………………………………………………..

## III. Mettre à jour des données dans une table
Syntaxe d’une requête SQL permettant de modifier des données stockées dans une table :
```sql
UPDATE table SET attribut1 = valeur1, ... WHERE sélection;
```
**Exemple :**
Compléter les requêtes suivantes : 

3.	Objectif de la requête : affecter M. Latouche comme professeur principal dans l’élève DUCOBU ;

Requête SQL : …………………………………………………………………………………………………………………………………………………..
 
4.	Requête SQL : ```UPDATE Prof SET salle = ’Musique’ WHERE nom = ’Rateau’``` ;

Objectif de la requête  : ….………………………………………………………………………………………………………………………………..

5.	Requête SQL : ```UPDATE prof SET num_prof = 3 WHERE nom = ‘Latouche’``` ;

Objectif de la requête  : ….………………………………………………………………………………………………………………………………..

Problème rencontré : ……………………………………………………………………………………………………………………………………..

## IV. Supprimer des données dans une table
Syntaxe d’une requête SQL permettant de supprimer des données stockées dans une table :
```sql
DELETE FROM table WHERE Sélection;
```
**Exemple :**
1.	Objectif de la requête : Supprimer l’élève Leonie Gratin 

Requête SQL : …………………………………………………………………………………………………………………………………………………..

2.	Requête SQL : ```DELETE FROM prof```

Objectif de la requête  : ….………………………………………………………………………………………………………………………………..
