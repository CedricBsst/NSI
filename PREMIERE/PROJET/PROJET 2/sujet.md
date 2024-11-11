# Projet Python : Jeu du Chifoumi (Pierre-Papier-Ciseaux)

## Objectif du projet

L’objectif de ce projet est de créer un programme en Python qui permet de jouer au **Chifoumi** (Pierre-Papier-Ciseaux) contre l’ordinateur. 

Le programme sera divisé en étapes claires avec des fonctions pour structurer le code.

---

## Règles du jeu

Le jeu oppose deux joueurs : l’utilisateur et l'ordinateur. Chacun choisit entre trois options :
- **Pierre**
- **Papier**
- **Ciseaux**

Les règles pour déterminer le gagnant sont les suivantes :
- **Pierre bat Ciseaux** (Pierre gagne)
- **Ciseaux bat Papier** (Ciseaux gagne)
- **Papier bat Pierre** (Papier gagne)
- Si les deux joueurs font le même choix, c’est une **égalité**.

---

## Consignes

Vous allez construire le programme étape par étape, en suivant les instructions pour coder chaque fonction nécessaire au jeu. 

### Étapes de réalisation et fonctions

1. **Fonction d’introduction**  

   Affiche un message d’introduction pour expliquer les règles et le déroulement du jeu.

2. **Fonction pour demander le choix de l'utilisateur**

    Demande au joueur ce qu'il souhaite jouer et renvoie son choix

3. **Fonction pour générer le choix aléatoire de l'ordinateur**

    Renvoie une valeur aléatoire parmi "Pierre", "Feuille" et "Ciseaux". Ce qui correspondra au choix de l'ordinateur

4. **Fonction de comparaison des choix**

    Prend en paramètre le choix de l'utilisateur ainsi que le choix de l'ordinateur et renvoie "joueur" si le joueur à gagné, "ordi" si l'ordinateur a gagné et "égalité" s'il y a égalité.

5. **Fonction permettant demandant à l'utilisateur s'il souhaite rejouer**

    Demande à l'utilisateur s'il souhaite faire une nouvelle manche. Votre fonction renvoie un booléen.

6. **Programme principal**

    En vous aidant des fonction précédemment réalisées, écrire le code de votre jeu.

    - L'utilisateur doit pouvoir réaliser plusieurs manche jusqu'à ce qu'il ne souhaite plus rejouer.
    - Une fois toutes les manches terminer, le jeu affiche le score final (nombre de partie gagné, nombre de partie perdu et nombre de partie à égalité).

## Barème
|Critère|Description|Points|
|-|-|-|
|1. Fonctionnement de base|||
|Saisie et affichage de choix|L’utilisateur peut saisir son choix, et le choix de l’ordinateur est affiché|3|
|Comparaison et résultat|Le programme compare les choix et affiche le bon résultat pour chaque manche|3|
|2. Fonctionnalités avancées|||
|Score et victoire finale|Le programme garde et affiche le score final|2|
|Boucle pour plusieurs manches|Le programme permet à l’utilisateur de rejouer plusieurs manches|3|
|3. Qualité du code|||
|Utilisation des fonctions|L’élève utilise des fonctions pour organiser le code|3|
|Clarté et lisibilité|Le code est bien organisé, avec des commentaires si nécessaire|2|
|4. Originalité et effort|		
|Effort et créativité|Personnalisation (messages originaux, variantes de règles, etc.)|2|
|Investissement||2|