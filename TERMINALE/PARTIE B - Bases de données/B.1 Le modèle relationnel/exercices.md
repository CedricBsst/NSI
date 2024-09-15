# Fiche d'exercices - **Chapitre B.1 - Le modèle relationnel**

## Exercice 1
Un particulier a un grand nombre de chansons stockées sur son ordinateur.
Il tient à jour un fichier qui contient toutes les chansons enregistrées par des groupes.

Ce fichier contient quatre colonnes où sont notés respectivement le titre de la chanson, le groupe qui l’a enregistrée, les membres du groupe et la date d’enregistrement.

Voici une ligne de ce fichier :

|Titre|Groupe|Membres|Année|
|-|-|-|-|
|Roxanne|The Police|Sting, Summers, Copeland|1978|

Écrire un schéma relationnel permettant permettant de stocker toutes ces données à l’aide de trois table nommées Chansons, Groupes et Artistes

## Exercice 2
Un commerçant utilise plusieurs fichiers pour gérer ses produits. On considère un fichier destiné à gérer des produits frais. Le tableau présenté est un extrait du contenu de ce fichier. Les quatre colonnes contiennent respectivement un identifiant numérique, le nom d’un produit, son prix et la marque qui le commercialise. Les mêmes noms de marques peuvent apparaître de nombreuses fois dans la colonne marque mais aussi dans les fichiers correspondant à d’autre types de produits.

|id|nom|prix|Marque|
|-|-|-|-|
|17|Yaourt6|2.52|Yopnone|
|21|Yaourt12|4.93|Dalait|
|25|Beurre250|2.28|Presement|
|28|Crème50|2.74|Dalait|
|31|Crème70|3.79|Yopnone|

1. A partir de ce fichier construire une relation Frais (pour les produit frais) et une relation Marques suivant le
modèle relationnel permettant d’éviter la redondance d’informations
2. Faire le schéma relationnel.

## Exercice 3
Un institut a constitué un tableau contenant les données statistiques concernant l'épidémie de COVID-19 sur une année. Ce tableau est constitué de quatre colonnes représentant : 
- Le nom du pays
- Le numéro du jour 
- Le nombre de cas confirmés
- Le nombre de décès

Voici quatres lignes extraites du tableau.
|pays|jour|cas|décès|
|-|-|-|-|
|France|83|1195|186|
|Allemagne|87|966|53|
|Suisse|95|228|17|
|France|108|2866|441|

Donner un exemple de clé primaire qui conviendrait pour cette table.

## Exercice 4
Deux relations modélisent la flotte de voitures d'un réseau de locations de voitures.

**voitures**
|id_voitures|marque|modèle|kilométrage|couleur|id_agence|
|-|-|-|-|-|-|
|1|Renault|Clio|12000|Rouge|2|
|2|Peugeot|205|22000|Noir|3|
|Toyota|Yaris|33000|Noir|3|

**agences**
|id_agence|ville|département|
|-|-|-|
|1|Paris|75|
|2|Lyon|69|
|3|Marseille|13|
|4|Aubagne|13|

1. Combien d'attributs possède la relation **voitures** ?
2. Dans la relation **voitures**, quel est le domaine de l'attribut **id_agence** ?
3. Réaliser le schéma relationnel de la base de données.
4. Quelle est la clé primaire de la relation **agence** ?
5. Quelle est la clé primaire de la relation **voitures** ?
6. Quelle est la clé étrangère de la relation **voitures** ? Quelle clé primaire référence-t-elle ?

## Exercice 5
On dispose de données, écrites dans un tableur concernant les vols qui sont prévus dans un aéroport pendant une journée.

Nous avons : 
- Le numéro du vol
- Les heures de départ et d'arrivée
- La provenance pour les vole à l'arrivée et la destination pour les vols au départ.
- Le type d'avion et sa capacité totale en passagers.
- Chaque vol dispose d'un numéro unique.

**Extrait du tableau**
|vol|HD|HA|Provenance|Destination|Avion|Capacité|
|-|-|-|-|-|-|-|
|AF273|8:45|10:05||Paris-France|Airbus A320|150|
|LX529|11:45|12:50|Genève-Suisse||Boeing 747|424|

1. Décrire six relations (Départ, Arrivée, Villes, Pays, Avion, Constructeurs) construites à partir de ce fichier permettant de satisfaire au modèle relationnel.

2. Donner un extrait des données de chacune des relations en vous basant sur les données du tableau précédent.
