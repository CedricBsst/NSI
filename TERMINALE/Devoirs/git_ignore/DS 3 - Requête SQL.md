# Devoir 3 - Requête SQL simple

Une entreprise de développement logiciel souhaite mettre en place une base de données pour suivre l'ensemble de ces projets de développement.

Lorsqu'un client commande un projet, celui-ci est affecté à une équipe de développeurs.

Pour faire cela, l'entreprise utilise trois relations : (```Projets```, ```Clients```, ```Equipes```).

Projets(**id_projet**, nom_projet, description_projet, #id_client, #id_equipe)  
Clients(**id_Client**, nom_client)  
Equipes(**id_equipe**, nom_equipe, nb_developpeur)  

Ci-dessous, on donne un extrait des tables de la base de données :

**Projets**
|id_projet|nom_projet|description_projet|id_client|id_equipe|
|-|-|-|-|-|
|1|"Cool RTT"|"Dev. d'un logiciel pour la gestion des RTT de l'entreprise"|1|1|
|2|"Conf. BAL"|"Dev. d'un configurateur de boîte aux lettres en ligne pour les commandes clients"|1|2|
|3|"Devis+"|"Logiciel de génération de devis automatique"|2|1|
|4|"Locker"|"Programmation des lockers de livraison"|2|3|

**Clients**
|id_client|nom_client|
|-|-|
|1|"Le bélier"|
|2|"Ozon"|

**Equipes**
|id_equipe|nom_equipe|nb_developpeur|
|-|-|-|
|1|interne1|4|
|2|interne2|3|
|3|externe3|10|

>**QUESTION 1**
>
> **(a)** Préciser pour la relation Projets, le nom de la clé primaire.
>
> **(b)** Quelles règles doit respecter un attribut pour pouvoir être choisi comme clé primaire ?

>**QUESTION 2**
>
> Préciser pour la relation Projets quel est le rôle de l'attribut _id_client_.

> **QUESTION 3**
>
> En vous basant sur les extraits de la base de données, indiquer ce qui sera renvoyé par la requête suivante : 
> ```sql
> SELECT id_projet, nom_projet
> FROM projets
> ```

> **QUESTION 4**
>
> Ecrire une requête permettant d'obtenir la description du projet "Cool RTT".

> **QUESTION 5**
>
> Expliquer par une phrase en Français ce que fais la requête suivante : 
> ```sql
> SELECT nom_projet, id_equipe
> FROM Projets 
> WHERE id_clients = 1;
> ```

> **QUESTION 6**
> Ecrire une requête permettant d'obtenir le nom des équipes ayant plus de 5 développeurs.

> **QUESTION 7**
>
> Expliquer par une phrase en Français ce que fais la requête suivante : 
> ```sql
> SELECT MAX(nb_developpeur)
> FROM Equipe
> ```

> **QUESTION 8**
>
> En utilisant la fonction ```COUNT``` et la clause ```GROUP BY```, écrire une requête permettant d'obtenir le nombre de projet par client.

>**QUESTION 9 (bonus)**
>
> L'entreprise souhaite pouvoir gérer individuellement chacun des développeurs.
>
> Proposer un nouveau schéma relationnel de la base de données en incluant une nouvelle table _Developpeurs_ contenant les identifiants, noms et prénoms de chacun d'entre eux.
>
> Chaque développeur appartient à une seule équipe.