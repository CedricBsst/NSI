1.  (a) id_projets
    (b) unique et non null

2. id_client est une clé étrangère qui référence la clé primaire de la table clients

3. 

|id_projet|Nom_projet|
|-|-|
|1|"Cool RTT"|
|2|"Conf. BAL"|
|3|"Devis+"|
|4|"Locker"|

4. 
```sql
SELECT description_projet
FROM projets
WHERE nom_projet = "Cool RTT";
```

5. Seléctionne le nom et le numéro d'équipes de projets qui concernent le client 1

6. 
```sql
SELECT nb_developpeur, nom_equipe
FROM equipes
WHERE nb_developpeur > 5;
```

7. Seléctionne le nombre de développeurs de l'équipe ayant le plus de développeurs

8. 
```sql
SELECT COUNT(*), id_client
FROM projets
GROUP BY id_client
```

9. 
Projets(id_projet, nom_projet, description_projet, #id_client, #id_equipe)
Clients(id_Client, nom_client)
Equipes(id_equipe, nom_equipe)
Developpeurs(id_dev, nom_dev, prenom_dev)
Appartenir(**#id_equipe**, **#id_dev**)