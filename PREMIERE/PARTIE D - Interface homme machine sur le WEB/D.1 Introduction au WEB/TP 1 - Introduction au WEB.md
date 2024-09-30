# Chapitre D.1 - Introduction au WEB
# TP 1 
## I. Histoire du WEB
Le **World Wide Web** (**WWW** ou **WEB**) est une application d'internet. Il s'agit d'un système hypertexte. Le WEB est a été développé au CERN (Conseil Européen pour la Recherche Nucléaire) par **Tim Berners-Lee** en 1989.

Le système hypertexte est un système permettant de consulter d'autres documents à partir d'un premier document en cliquant sur des mots. Ces mots cliquables sont appelés des hyperliens.

La première page WEB est toujours consultable à l'adresse suivante : http://info.cern.ch/hypertext/WWW/TheProject.html.

## II. Écriture d'une page WEB
Pour écrire une page WEB, on utilise trois langages : 
- HTML (Contenu de la page)
- CSS  (Design de la page)
- JavaScript (Langage de script permettant de rendre la page plus dynamique)

Dans ce premier TP, nous nous arrêterons sur les langage HTML et CSS uniquement.

### A. Le langage HTML
#### Les bases du langage HTML
Le langage HTML (HyperText Markup Language - _Langage de balises pour l'hypertexte_) est utilisé dans le but de créer le contenu et la structure des pages WEB. 

Le langage HTML utilise des balises pour structurer le contenu d'une page. Chaque balise a un rôle prédéfinit par le language HTML. (**Exemple :** ```<title>```, ```<h1>```).

> **QUESTION 1**
>
> Ouvrir la première page du WEB, en utilisant le menu "outils de développement" de votre navigateur (touche ```F12```sur le navigateur Chrome) vous avez accès au code HTML de la page.
> Déterminer quelles balises permettent de définir :
> - Le titre de la page WEB
> - Un titre
> - Un paragraphe
> - Un lien

> **QUESTION 2**
>
> Déterminer le rôle des balises suivantes :
> - ```<head>```
> - ```<body>```
> - ```<header>```

Comme vous avez pu le remarquer, chaque balise ouverte ```<balise>``` est associée à une balise fermante ```</balise>```. En effet, chaque balise ouvrante doit être accompagné d'une balise fermante. Entre ces deux balises, on écrit le contenu de la page WEB correspondant. 

**Exemple :**
```html
<p> J'écris un paragraphe </p>
```
La balise ouvrante ```<p>``` permet de définir que ce qui va suivre sera un paragraphe, elle est associé à une balise fermante ```</p>``` qui indique que le paragraphe est terminé.

Il est possible d'imbriquer les balises les unes dans les autres lorsque cela est nécessaire, il faut cependant vérifier à fermer les balises dans le bonne ordre.

**Exemple :**
```html
<h1> Ce code <em>HTML est incorrect</h1></em>
```
**La balise ```<em>``` ouverte après ```<h1>``` doit être fermé avant la balise fermante ```</h1>```**

```html
<h1> Ce code <em> HTML est correct</em></h1>
``` 

>**QUESTION 3**
>
>Parmi les codes HTML suivant, lesquels sont bien écrits ?
>```html
> <h1>Ceci est un titre</h1>
> <p>Bonjour</p>
> <p>Vous allez bien ?</p>
> ```
>
> ```html
> <h1><p>Ceci est un titre</p></h1>
> <p>Vous allez bien ?</p>
> ```
>
> ```html
> <h1><p>Ceci est un titre</h1>
> <p>Vous allez bien ?</p></p>
>```
>
>``` html
> <h1>Ceci est un titre</h1>
> <p>Bonjour</p>
> <p id="para_1">Vous allez bien ?</p>

> **QUESTION 4**
> 
> Ouvrir un document sur lequel vous créerez votre memo HTML. 
> Pour chaque nouvelle balise que vous rencontrerez dans la suite du TP, vous l'ajouterez à votre memo. 
>  
> Vous catégoriserez les éléments de votre memo de façon à retrouver les balises que vous rechercher plus facilement dans celui-ci. (STRUCTURE DU DOCUMENT, INFORMATIONS DE LA PAGE, BALISES DE STRUCTURES, LIENS, STRUCTURATION DU TEXTE, TABLEAUX, LISTES, FORMULAIRES)
> **Exemple :**
>
> **STRUCTURATION DU TEXTE :**
> |balise|rôle|attribut|
> |-|-|-|
> |p|paragraphe||
>
> **INFORMATIONS DE LA PAGE**
> |balise|rôle|attribut|
> |-|-|-|
> |title|titre de la page web||
>
> Laisser les cases attribut vide pour le moment.

> **QUESTION 5**
>
>Dans la suite du TP, nous allons écrire une page HTML simple. 
>
>Pour cela, créer un nouveau fichier texte. Modifier l'extension ```.txt``` en ```.html```

Pour modifier votre fichier, ouvrez le avec Notepad++

Pour voir votre page WEB, ouvrez le fichier avec un navigateur. 

#### Structurer son document
Lorsque l'on écrit un document HTML, on doit indiquer au navigateur la version HTML utilisé. Pour cela, on met un doctype du document au début du fichier.

Pour HTML 5 (version le plus récente) il faut écrire ceci : 
```!DOCTYPE html>```

>**QUESTION 5 :**
>
>Ajouter le doctype sur votre document

La structure d'une page web est constitué de la façon suivante : 

```html
<html>
    <head>
        <title>Titre de la page</title>
        <meta charset="utf-8">
    </head>
    <body>
        <header>
        </header>
        <section>
        </section>
        <section>
        </section>
        ...
        <footer>
        </footer>
    </body>
</html>
```
- ```<html>``` permet de définir le code html
- ```<head>``` permet de définir l'en-tête du document. C'est ici que l'on définit les méta-données.
- ```<meta>``` permet d'ajouter des métadonnées. Il s'agit d'une balise particulière car elle ne nécessite pas de balise fermante. Ici, on définit le système d'encodage utilisé pour notre page WEB. Vous comprendrez mieux de quoi il s'agit plus tard dans l'année.
- ```<body>``` permet de définir le corps du document, son contenu
- ```<header>``` permet de définir un contenu introductif. Généralement le haut de page du document.
- ```<section>``` permet de définir une section du document.
- ```<footer>``` permet de définir le pied de page (ou le pied d'une section)

> **Question 6 :**
>
> Ajouter la structure d'une page WEB à votre fichier. Nous n'utiliserons qu'une section.
> 
> Le titre de notre page WEB sera "Introduction au WEB"

#### Écrire du texte
Pour le moment, lorsque nous affichons la page dans un navigateur. Rien n'apparaît, en effet notre page est structurée mais ne contient aucun contenu.

> **Question 7 :**
>
>Entre la balise ouvrante ```<header>```et la balise fermante ```</header>```, ajouter le code suivant :
> ```html 
> <h1>Apprentissage du HTML et du CSS</h1>
> ```

La balise ```<h1>``` permet de définir un titre de niveau 1. En HTML, il existe 6 niveaux de titre (```<h1>```, ```<h2>```, ```<h3>```, ```<h4>```, ```<h5>```, ```<h6>```). ```<h1>``` étant un titre de très grande importance et ```<h6>```étant un titre de petite importance.

> **QUESTION 8 :**
>
> Ajouter au sein de votre section la structure de titre suivante : 
> 
> I. L'histoire du WEB
>
> II. Le protocole HTTP
>
> III. Les langages du WEB
>
> A. Coté client
> 
> B. Coté serveur


Pour ajouter des paragraphes, on utilise la balise ```<p>```. 

>**QUESTION 9 :**
>
>La première partie de notre page WEB concerne l'histoire du WEB. Recopier en utilisant 3 paragraphes l'introduction de ce TP concernant l'histoire du WEB sur votre page.

Comme vous avez pu le remarquer, notre texte initial contient des éléments en gras. Cela signifie qu'il sont plus important. En html, pour indiquer qu'un texte a une importance particulière, on utilise la balise ```<strong>```.

**Exemple :**
```html
<p>Ce <strong>groupe de mots</strong> et plus important que ce groupe de mots</p>.
```
> **QUESTION 10 :**
>
> Utiliser la balise ```<strong>``` pour mettre en avant le texte qui était déjà en gras sur le TP.

#### Liens et attributs de balise
Notre introduction contient un lien vers la première page WEB mise en ligne.

Pour ajouter un lien, on utilise la balise ```<a>```.

**Exemple :** 
```html
<a>mon lien</a>
```

En écrivant ceci, votre lien ne fonctionnera pas. En effet, le texte contenu entre les balises ```<a>``` et ```</a>``` indique le texte à afficher sur le navigateur mais celui-ci ne connaît pas la page vers laquelle notre lien doit pointer. 

Pour l'indiquer, nous utilisons l'attribut ```href```.

> Un attribut est un paramètre que l'on peut ajouter au balise. Un attribut correspond a un nom que l'on associe a une valeur. Ils permettent d'ajouter des informations pour le bon fonctionnement de la balise. 
>
> Par exemple :
>
> - Dans le cas d'un lien, l'attribut ```href``` permet d'indiquer la page vers laquelle le lien doit pointer.
> - Dans le cas de la balise ```<meta>``` que nous avons utilisé plus haut, l'attribut ```charset``` permet de définir le système d'encodage utilisé.
> - L'attribut ```id``` est utilisable sur tous les types de balises et permet de leur associer un identifiant unique lorsque cela est nécessaire.

Ainsi, pour indiquer qu'un lien pointe vers la page WEB de GOOGLE, il faut écrire : 
```html
<a href="www.google.com">mon lien</google>
```
> **QUESTION 11 :**
>
> Utiliser la balise ```a``` pour ajouter le lien dans votre paragraphe

#### Ajouter des images
> **QUESTION 12 :**
>
> Dans la partie II, ajoutez le code HTML suivant :
> ```html 
> <p><strong>HTTP</strong> - <strong>HyperText Transfer Protocol</strong> - (Protocole de transfert hypertexte) et un protocole de communication développé pour le WEB.</p>
> <p><strong>HTTPS</strong> (S signifie Secure) est sa version sécurisé. En effet à l'inverse du protocole HTTP, les communications effectuées avec le protocole HTTPS sont chiffrées.</p>
> <p> Dans l'illustration suivante, une requête HTTP est envoyée pour récupérer la page d'accueil du site <a href="www.perdu.com">perdu.com</a></p>

On souhaite ajouter une image en dessous du dernier paragraphe. Pour ajouter une image, il faut utiliser la balise ```<img>```. On indique le chemin de l'image à l'aide de l'attribut ```src```. 

La balise ```<img>``` n'a pas besoin d'être fermée. On dit qu'elle est auto-fermante.

**Exemple :**
```html
<img src="mon_image.jpg">
```

>**QUESTION 13 :**
>
> Télécharger l'image ```http_exemple.png``` situé dans le dossier ```media``` sur le github.
> 
> Sauvegarder l'image sur votre ordinateur dans le même dossier que votre page WEB
>
> Ajouter le code HTML suivant dans votre page WEB en dessous du dernier paragraphe que vous avez ajouté.
> ```html
> <img src="http_exemple.png">
> ```

> **QUESTION 14 :**
> 
> Ajouter une photo du chercheur Tim Berners-Lee pour étoffer votre introduction.

#### Faire des listes
> **QUESTION 15 :**
> Dans la partie "A. Coté client", ajouter les paragraphes suivants : 
> 
> "Dans un modèle client serveur, le client est celui qui demande une ressource. Sur le WEB, le client est donc le navigateur WEB (Chrome, SAFARI, EDGE, Firefox ...). "
>
> "Le rôle du navigateur est d'envoyer des requêtes HTTP au serveur, et d'afficher la réponse de celui-ci. "
>
> "Le navigateur est capable de comprendre trois langages : (HTML, CSS et JavaScript)"
>
> "Ces codes sont exécutés et traiter par le client (le navigateur)."

Nous souhaitons afficher les trois langages du WEB sous la forme d'une liste, comme ceci :
- HTML
- CSS
- JAVASCRIPT

Il existe deux balises permettant de faire des listes, ```<ul>``` et ```<ol>```. Ces deux balises permettent de définir une liste complète pour définir une élément dans la liste, on utilise la balise ```<li>```.

>**QUESTION 16 :**
>
>Tester les deux codes suivants, expliquer la différence entre les deux types de liste et modifier votre code HTML pour que les trois langages (HTML, CSS et Javascript) apparaissent sous la forme d'une liste en choisissant le type de liste qui vous paraît le plus adapté.
> ```html
> <ul>
>     <li>item 1</li>
>     <li>item 2</li>
>     <li>item 3</li>
>     <li>item 4</li>
> </ul>
> ```
>
> ```html
> <ol>
>     <li>item 1</li>
>     <li>item 2</li>
>     <li>item 3</li>
>     <li>item 4</li>
> </ol>
> ```

> **QUESTION 16 :**
>
> Ajouter le code HTML suivant dans la dernière partie de votre page WEB pour terminer l'écriture de votre cours.
>
> ```html
> <p>Lorsque le serveur reçoit une requête HTTP, il renvoie la page WEB demandé, c'est à dire les tous fichiers dont le navigateur aura besoin pour afficher la page (HTML, CSS, Javascript, images)</p>
><p>En utilisant un langage de programmation, le serveur est capable d'adapter la page WEB en fonction de la demande du client. Pour ce faire, il est possible d'utiliser n'importe quel langage de programmation. (Python, Ruby, NodeJS...). Cependant, le langage WEB le plus utilisé côté serveur et le langage <strong>PHP</strong> (hypertext processor)</p>
> ```

### B. Le langage CSS