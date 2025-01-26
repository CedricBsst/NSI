# Projet 3 - IceWalk

## Description

Marcher sur la glace est un exercice périlleux :
- on ne peut pas changer de direction,
- il est difficile de s’arrêter.

Dans ce projet, nous allons nous intéresser à la programmation d’un jeu dans lequel le joueur incarnera un personnage se déplaçant sur la glace.

### Terrain

Le terrain est :
- rectangulaire
- entièrement constitué de cases gelées, à l’exception d’une seule case appelée case finale. Certaines cases sont des murs.
- entouré de murs.

### Règles du Jeu

À chaque étape du jeu, le joueur choisit un personnage et une direction parmi quatre (Nord, Sud, Est, Ouest) pour le personnage choisi.

Ce dernier se déplace alors dans la direction choisie en ligne droite jusqu’à rencontrer un obstacle.

### Fin du Jeu

Le jeu se finit lorsque :
- le joueur principal est arrivé sur la case finale;
- il abandonne la partie (il n’est parfois plus possible de rejoindre la case finale si une mauvaise direction a été prise).

## Etapes du jeu

### ETAPE 1 - Représentation et affichage du terrain
Créer une représentation du terrain et afficher la grille avec les cases gelées, les murs et la case finale.

- Quelles structures de données ?
- Comment représenter le joueur ?
- Comment charger plusieurs niveaux ?

### ETAPE 2 - Gestion des déplacements et des collisions
Implémenter la logique de déplacement des personnages et gérer les collisions avec les murs et les bords du terrain.

- Quels sont les directions possibles ?
- Comment faire avancer le joueur jusqu'au prochain mur ?
- Quels sont les conditions de victoire ?

### ETAPE 3 - Gestion des scores
Ajouter un système de score pour suivre les performances du joueur principal et des autres personnages. Les scores seront conservés dans une base de données

- Comment charger les meilleurs scores pour les comparer au nouveau score ?
- Comment mettre à jour la table des meilleurs scores ?

> Proposez un schéma relationnel pour votre projet, le professeur vous donnera le code SQL permettant de créer la base.

### ETAPE 4 - Résolution automatique
Développer un algorithme pour résoudre automatiquement le jeu en trouvant le chemin optimal vers la case finale.

- Comment trouver le meilleur chemin ?
  
> Utilisez les algorithmes vus sur les graphes.

## Notation

Chacune des étapes sera notée sur 5. À la fin de chaque étape, chaque groupe passera au tableau pour montrer son avancement dans le projet.

### Grille de notation

| Etape | Critère                        | Description                                                                  | Points |
|-------|--------------------------------|------------------------------------------------------------------------------|--------|
| 1     | Choix de la structure de données | Le choix de la structure de projet utilisée est pertinent et argumenté     | 1      |
|       | Représentation du joueur        | Représentation correcte du joueur sur la grille                             | 1      |
|       | Gestion de plusieurs niveaux    | Capacité à charger plusieurs niveaux                                        | 1      |
|       | Investissement                  | Participation active et implication dans le projet                          | 0.5    |
|       | Prestation orale                | Clarté et qualité de la présentation orale                                  | 0.5    |
| 2     | Directions possibles            | Gestion correcte des directions possibles                                   | 1      |
|       | Déplacement jusqu'au mur        | Déplacement correct jusqu'au prochain mur                                   | 1      |
|       | Conditions de victoire          | Définition et gestion des conditions de victoire                            | 1      |
|       | Investissement                  | Participation active et implication dans le projet                          | 0.5    |
|       | Prestation orale                | Clarté et qualité de la présentation orale                                  | 0.5    |
| 3     | Chargement des scores           | Capacité à charger les meilleurs scores                                     | 1      |
|       | Mise à jour des scores          | Mise à jour correcte de la table des meilleurs scores                       | 1      |
|       | Schéma relationnel              | Proposer un schéma relationnel approprié                                    | 1      |
|       | Investissement                  | Participation active et implication dans le projet                          | 0.5    |
|       | Prestation orale                | Clarté et qualité de la présentation orale                                  | 0.5    |
| 4     | Algorithme de recherche         | Utilisation correcte des algorithmes de recherche                           | 2      |
|       | Chemin optimal                  | Capacité à trouver le chemin optimal                                        | 1      |
|       | Investissement                  | Participation active et implication dans le projet                          | 0.5    |
|       | Prestation orale                | Clarté et qualité de la présentation orale                                  | 0.5    |

