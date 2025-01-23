# Fiche d'exercices - **Chapitre B.4 - Requêtes de mise à jour**
On crée dans la base monMagasin la relation :

```sql 
CREATE TABLE Article ( categorie enum(’alimentaire’,
                       ’quincaillerie’,
                       ’droguerie’,
                       ’hygiene’) NOT NULL DEFAULT ’alimentaire’, 
                       nom VARCHAR(65) NOT NULL DEFAULT ’’, 
                       marque VARCHAR(65) NOT NULL DEFAULT ’’,
                       codeBarre INT NOT NULL DEFAULT 0, 
                       prix FLOAT(4,2) DEFAULT NULL,
                       quantite INT NOT NULL DEFAULT 0 
                       PRIMARY KEY (codeBarre)
                     ); 
```
1.	Ecrire la requête qui affiche toutes les occurrences de la table ´ Article. 

2.	Faire afficher tous les noms et prix des articles de la marque ”TopMark” du moins cher au plus cher. 

3.	Ecrire la requête qui affiche les noms des articles qui ne sont plus en stock.  

4.	Un client vient d’acheter 2 savons de Marseille ”monsavon” sachant qu’il y avait en stock 25 savons, écrire la requête permettant de modifier l’information.

5.	Que fait la requête : 
```sql 
SELECT marque 
WHERE nom 
LIKE ’%brioche%’.
```
6.	Le prix de l’article dont le code-barre est 3005000000000 passe de 15 à 15,7 Euros, écrire la requête qui réalise la modification. 

7.	Faire afficher les codes-barres des articles qui sont dans la catégorie ”hygiene”.

8.	Faire afficher tous les articles dont le prix est supérieur à 100 Euros. 

9.	Faire afficher les articles de la catégorie ”droguerie” dont le nom contient le mot ”soude”. 

10.	Le code barre est un entier à 13 chiffres, faire afficher les articles dont le code barre commence par 25. 

11.	Le magasin qui doit subir des rénovations va supprimer tous les articles de quincaillerie, écrire la requête nécessaire à cette action. 

12.	Que fait cette requête ? 
```sql
SELECT nom,prix,quantité 
WHERE categorie=’alimentaire’
AND nom LIKE ’Sau%’ 
```

13.	On a rangé les articles pour animaux dans le rayon ”quincaillerie”, écrire une requête qui affiche toutes les marques qui fabriquent des croquettes pour chiens ou chats.
