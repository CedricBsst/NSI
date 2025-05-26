# TP - Les formulaires WEB

## C'est quoi un formulaire ?

Dans une page WEB, un formulaire permet à l’utilisateur de saisir des valeurs qui ont pour but d’être traitées par le serveur. Vous utilisez par exemple un formulaire WEB lorsque vous vous inscrivez sur un site internet.

## Construction d'un formulaire

### Création du formulaire

Un formulaire se délimite par la balise `form`. Cette balise prend deux attributs, un attribut `method` et un attribut `action`.

1. Créer un fichier HTML mon\_formulaire.html contenant les balises permettant de définir une page WEB minimale (`html`, `head`, `body`, etc…)
2. Ajouter une balise `form` dans votre `body`.

   * L’attribut `method` prendra la valeur `POST`
   * L’attribut `action` prendra la valeur `./mon_formulaire.html`

### La balise input

3. Recopiez le code html suivant dans votre formulaire, puis vérifier le résultat

```html
<label for="prenom">Entrez votre prénom</label>
<input type="text" name="prenom" id="prenom"/>
```

* La balise `label` permet de définir le libellé d’un champ.

  * L’attribut `for` permet de spécifier l'id du champ lié au libellé.
* La balise `input` permet de définir un champ du formulaire.

  * L’attribut `type` permet de définir le type de champ.
  * L’attribut `name` permet de spécifier le nom du du champs qui sera utilisé lors du traitement des données
  * L’attribut `id` permet de donner un identifiant à l’élément html

#### Les différents type de champs

Jusqu’à présent nous avons vu le type `text` permettant d’obtenir un champ de saisie dans lequel l’utilisateur peut saisir un texte. Il existe un très grand nombre de types de champs qu’il est possible d’utiliser dans une balise `input`. Dans la suite de ce TP nous verrons les types les plus couramment utilisés.

---

4. Définir un nouveau champ de saisie avec le type `password` et testez-le.
5. Quelle est la différence entre un champs de type `password` et un champ de type `text` ?

---

6. Copiez le code HTML suivant à la suite de votre champ password et testez-le.

```html
<p>Aimes tu la NSI ?</p>
<input type="radio" name="like" id="like_oui" value="oui"/>
<label for="like_oui">oui</label>
<input type="radio" name="like" id="like_non" value="non"/>
<label for="like_non">non</label>
```

7. Que permet de faire un `input` de type `radio` ?
8. Que se passe-t-il lorsque l'on sélectionne l'un des deux champs alors que l'autre est déjà sélectionné ?
9. Comment le navigateur peut déterminer que ces deux champs sont liés ?
10. Selon vous, que permet de faire l’attribut `value` ?

---

Un champ de type `checkbox` permet définir une case que l’utilisateur peut cocher ou non.

11. Créer un nouveau champ de type `checkbox` qui permettra de demander à un utilisateur s’il sera présent lors de la prochaine réunion.
12. Modifier le comportement par défaut de votre champ pour qu’il soit coché par défaut.

---

Un champ de type `button` permet de créer un bouton qui n’a aucun comportement défini par défaut. Nous verrons plus tard comment modifier son comportement à l’aide du langage JavaScript.

13. Créer un bouton. L’attribut `value` permet de définir le texte écrit dans le bouton, définissez le sur « clique ici ! »

---

Il existe d'autre type de bouton qui eux, ont un comportement défini.
14\. Créer un champ de type `reset` et testez-le. Que fait ce bouton ?

---

Un champ de type `submit` permet d’obtenir un bouton qui permet de valider le formulaire est d’envoyer les données au serveur.

15. Créer un bouton permettant de valider le formulaire

---

Il existe beaucoup d’autres types de champs permettant la saisie de données comme, par exemple, `date`, `file`, `tel` ou encore `email`.

### La balise select

Pour créer une liste déroulante, il faut utiliser un balise particulière, en effet, on n’utilise pas une balise `input` mais une balise `select`, puis à l’intérieur de cette balise, on ajoute des balises option qui contiennent chacune un élément de la liste déroulante.
16\.	Copiez et testez-le code HTML suivant

```html
<select name="prefere" id="prefere">
    <option value="Math">Mathématiques</option>
    <option value="NSI">NSI</option>
    <option value="Français">Français</option>
</select>
```

## Valider un formulaire

Reprenons l’attribut `action` de notre balise `form`, cet attribut permet de définir la ressource / page vers laquelle l’utilisateur sera ramené après la validation du formulaire, c’est lors du traitement de cette ressource que le serveur réalisera le traitement des données du formulaire. Ici nous avons mis la page de notre formulaire elle-même afin de toujours y revenir.

L’attribut `method`, quant à lui, permet de choisir le type de requête envoyée au serveur

17.

* Compléter le formulaire et validez-le, lire l’URL
* Modifier la valeur POST par la valeur GET de l’attribut method de la balise `form`, valider le formulaire puis vérifier l’URL. Quelle différence avez-vous remarquée entre les deux méthodes ?

---

## Introduction à JavaScript

HTML permet de structurer les pages, CSS de les mettre en forme, mais c’est JavaScript qui permet de les rendre interactives. Grâce à JavaScript, vous pouvez modifier le contenu d’une page sans avoir besoin de la recharger, réagir à des événements (clics, saisie de texte, etc.), valider des formulaires, créer des animations, etc.

### Insertion de JavaScript dans une page HTML

Il existe plusieurs manières d’intégrer du JavaScript :

1. **Directement dans une balise `<script>` dans le fichier HTML** :

```html
<script>
    alert("Bonjour !");
</script>
```

2. **Dans un fichier externe** :

```html
<script src="script.js"></script>
```

### Exemple simple : modifier un élément HTML

Ajoutez ce code dans votre fichier HTML :

```html
<button onclick="changerTexte()">Cliquez ici</button>
<p id="demo">Texte original</p>

<script>
    function changerTexte() {
        document.getElementById("demo").innerText = "Texte modifié !";
    }
</script>
```

### À vous de jouer !
18. Créez un bouton qui lorsqu'on clique dessus, change le texte d'un paragraphe
> - Ajoute un bouton dans la page HTML
> - Ajoute un paragraphe avec un id (par exemple monTexte).
> - Crée une fonction JavaScript qui modifie le texte du paragraphe grâce à `document.getElementById(...).innerText`.
> - Lien la fonction au clic du bouton avec l’attribut onclick.


19. Créez un bouton qui, lorsqu’on clique dessus, change la couleur de fond de la page.
> - Récupère la couleur du body avec `document.body.style`
> - Modifie la propriété backgroundColor

20. Ajoutez un champ texte et un bouton qui affiche une alerte contenant le texte saisi par l’utilisateur.
> - Crée un élément <input type="text"> avec un id.
> - Crée un bouton avec un onclick qui déclenche une fonction.
> - Dans cette fonction, récupère la valeur de l’input avec .value.
> - Affiche la valeur avec alert().

21. Essayez de récupérer la valeur d’un champ du formulaire avec JavaScript et de l’afficher dans un paragraphe.
> - Ajoute un paragraphe avec un id pour afficher le texte.
> - Dans ta fonction JavaScript, remplace alert() par une modification du contenu du paragraphe avec .innerText.

