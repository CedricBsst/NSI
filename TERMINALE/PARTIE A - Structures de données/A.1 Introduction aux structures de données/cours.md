# Chapitre A.1 : Introduction aux structures de données

## I. Définition 
Une **structure de données** est une manière d'organiser des données ayant pour objectif de traiter les données plus facilement.

Chaque structure de données est à envisager sous deux aspect :

- Son **interface** : <span class="caché"> L'interface est destiné à l'utilisateur de la structure de données, elle contient la *spécification* des méthodes que l'on peut appliquer à cette structure de données. </span>
- Son **implémentation** : <span class="caché">L'implémentation est une mise en œuvre pratique de la structure de données dans un langage de programmation.</span>

Par exemple, dans une voiture, les pédales et le volants constituent une partie de l'interface de la voiture. Tandis que l'implémentation correspondra plutôt aux mécanismes qui permettent à la voitures d'avancer, de freiner, de tourner etc...

Ainsi, il n'est pas nécessaire pour l'utilisateur d'une structure de données de connaître son implémentation pour pouvoir l'utiliser. Seul son interface est nécessaire.

## II. Les listes (```list``` en python)
Une liste est <span class="caché"> un ensemble d'élément ordonnés</span>. La liste est une structure de données qui existe dans une grande majorité des langages de programmation.

L'interface d'une liste est très similaire dans chacun des langages de programmation.  
L'implémentation d'une liste est propre à chaque langage.

En python les listes sont représentées par le type ```list```. 

### Interface d'une liste
- <span class="caché"> Créer une liste </span>
    - Paramètres : <span class="caché">AUCUN</span>
    - Renvoie : <span class="caché"> Une liste vide </span>
    - Conditions d'utilisation : <span class="caché"> AUCUN </span>
    - Effets de bord : <span class="caché">AUCUN</span>
    - Ecriture python : <span class="caché"> []</span>
- <span class="caché"> Ajouter un élèment </span>
    - Paramètres : 
        - <span class="caché">Une liste</span>
        - <span class="caché">Un élément </span>
    - Renvoie : <span class="caché">AUCUN</span>
    - Conditions d'utilisation : <span class="caché"> AUCUN </span>
    - Effets de bord : <span class="caché">l'élément est ajouté à la fin de la liste.</span>
    - Ecriture python : <span class="caché">l.append(e)</span>
- <span class="caché">Supprimer un élément</span>
    - Paramètres :
        - <span class="caché">Une liste</span>
        - <span class="caché">Un indice</span>
    - Renvoie : <span class="caché">l'élément supprimé </span>
    - Conditions d'utilisation : <span class="caché"> la liste doit contenir au moins autant d'éléments que l'indice passé en paramètre </span>
    - Effets de bords : <span class="caché">l'élément situé à l'indice passé en paramètre est retiré de la liste</span>
    - Ecriture python : <span class="caché">l.pop(i)</span>
- <span class="caché">Accéder à un élément</span>
    - Paramètres :
        - <span class="caché">Une liste</span>
        - <span class="caché">Un indice</span>
    - Renvoie : <span class="caché"> L'élément de la liste situé à l'indice passé en paramètre</span>
    - Conditions d'utilisation : <span class="caché"> la liste doit contenir au moins autant d'éléments que l'indice passé en paramètre </span>
    - Effets de bords : <span class="caché">AUCUN</span>
    - Ecriture python : <span class="caché">l[i]
- <span class="caché"> Modifier un élément</span>
    - Paramètres : 
        - <span class="caché">Une liste</span>
        - <span class="caché">Un indice</span>
        - <span class="caché">Une valeur</span>
    - Renvoie : <span class="caché">AUCUN</span>
    - Conditions d'utilisation : <span class="caché"> la liste doit contenir au moins autant d'éléments que l'indice passé en paramètre </span>
    - Effets de bords : <span class="caché">l'élément de la liste situé à l'indice passé en paramètre est remplacer par la valeur.</span>
    - Ecriture python : <span class="caché">l[i]=v</span>
- <span class="caché"> Connaître le nombre d'éléments</span>
    - Paramètres : <span class="caché">une liste</span>
    - Renvoie : <span class="caché">le nombre d'éléments de la liste</span>
    - Conditions d'utilisation : <span class="caché">AUCUN</span>
    - Effets de bords : <span class="caché">AUCUN</span>
    - Ecriture python : <span class="caché">len(l)</span>
## III. Les dictionnaires (```dict``` en python)
Un dictionnaires est une structure de données permettant de représenter <span class="caché"> une collection d'objets non ordonées. Il est composé de paires clef:valeur.</span>

### Interface d'un dictionnaire
- <span class="caché">Créer un dictionnaire</span>
    - Paramètres : <span class="caché">AUCUN</span>
    - Renvoie : <span class="caché">Un dictionnaire vide</span>
    - Conditions d'utilisation : <span class="caché">AUCUN</span>
    - Effets de bords : <span class="caché">AUCUN</span>
    - Ecriture python : <span class="caché">{}</span>
- <span class="caché">Ajouter un élément</span>
    - Paramètres : 
        - <span class="caché">Un dictionnaire</span>
        - <span class="caché">Une clé</span>
        - <span class="caché">Une valeur</span>
    - Renvoie : <span class="caché">AUCUN</span>
    - Conditions d'utilisation : <span class="caché">La clé n'existe pas dans le dictionnaire</span>
    - Effets de bords : <span class="caché">Le couple clé:valeur est ajouté au dictionnaire</span>
    - Ecriture python : <span class="caché">d[cle] = valeur</span>
- <span class="caché">Accéder à un élément</span>
    - Paramètres : 
        - <span class="caché">Un dictionnaire</span>
        - <span class="caché">Une clé</span>
    - Renvoie : <span class="caché">La valeur associé à la clé passée en paramètre</span>
    - Conditions d'utilisation : <span class="caché">La clé dans exister dans le dictionnaire</span>
    - Effets de bords : <span class="caché">AUCUN</span>
    - Ecriture python : <span class="caché">d[cle]</span>
- <span class="caché">Modifier un élément</span>
    - Paramètres : 
        - <span class="caché">Un dictionnaire</span>
        - <span class="caché">Une clé</span>
        - <span class="caché">Une valeur</span>
    - Renvoie : <span class="caché">AUCUN</span>
    - Conditions d'utilisation : <span class="caché">La clé doit exister dans le dictionnaire</span>
    - Effets de bords : <span class="caché">La valeur associée à la clé passée en paramètre est modifiée</span>
    - Ecriture python : <span class="caché">d[cle]=valeur</span>
- <span class="caché">Supprimer un élément</span>
    - Paramètres : 
        - <span class="caché">Un dictionnaire</span>
        - <span class="caché">Une clé</span>
    - Renvoie : <span class="caché">La valeur supprimée</span>
    - Conditions d'utilisation : <span class="caché">La clé doit exister dans le dictionnaire</span>
    - Effets de bords : <span class="caché">Le couple clé:valeur associé est supprimé</span>
    - Ecriture python : <span class="caché">d.pop(cle)</span>
- <span class="caché">Obtenir la liste des clés</span>
    - Paramètres : <span class="caché">Un dictionnaire</span>
    - Renvoie : <span class="caché">La liste des clés du dictionnaire</span>
    - Conditions d'utilisation : <span class="caché">AUCUN</span>
    - Effets de bords : <span class="caché">AUCUN</span>
    - Ecriture python : <span class="caché">d.keys()</span>
- <span class="caché">Savoir si une clé existe</span>
    - Paramètres :
        - <span class="caché"> Un dictionnaire</span>
        - <span class="caché"> Une clé
    - Renvoie : <span class="caché">Vraie si la clé est dans le dictionnaire et faux sinon.</span>
    - Conditions d'utilisation :<span class="caché">AUCUN</span>
    - Effets de bords :<span class="caché">AUCUN</span>
    - Ecriture python : <span class="caché">cle in d</span>