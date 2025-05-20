# Chapitre D.4 - Modularité
# TP - Utiliser une API

## Introduction 
Une API (Application Programming Interface), ou interface de programmations d'applications, est un ensemble de classes, de fonction, constantes grâce auquel un programme fournisseur met à disposition différentes fonctionnalités pour des programmes consommateurs.

C'est le programme fournisseur qui définit de quelle façon les fonctionnalités sont mises à disposition des consommateurs, en imposant éventuellement un certain nombre de contraintes d'accès à l'API.

- Une API fonctionne souvent grâce à des requêtes HTTP (les mêmes protocoles utilisés par les navigateurs web).
- Le programme client envoie une requête à l’API, généralement de type :
  - **GET :** pour demander des informations,
  - **POST :** pour envoyer des données au serveur.
- Le serveur répond avec des données, souvent au format JSON (un format texte structuré facile à lire par les ordinateurs).
- Le programme client peut alors utiliser ces données pour effectuer des actions ou les afficher.


## Activité 1
On s'intéresse ici à la Base Adresse Nationale qui est une API gratuite du gouvernement français permettant d'obtenir un certain nombre d'informations à partir d'une adresse postale.

L’API peut être interrogée simplement en envoyant une requête **GET** à une URL construite à partir de l’adresse souhaitée.

Par exemple, pour obtenir des informations sur l’adresse postale du lycée, on peut écrire l’URL suivante dans la barre d’adresse de votre navigateur : 

https://api-adresse.data.gouv.fr/search/?q=1-espace-jean-guerlandg&postcode=02200

> **Note :** En entrant cette URL dans votre navigateur, vous envoyez une requête HTTP au serveur. La réponse s’affiche alors sous forme brute au format JSON.

Maintenant que vous savez comment fonctionne l’API et comment tester une requête dans un navigateur, nous allons écrire un programme Python qui va :

- envoyer une requête à l’API Base Adresse Nationale,
- récupérer la réponse au format JSON,
- extraire et afficher certaines informations utiles.

### ETAPE 1 : Importer les modules nécessaires
Python possède un module intégré urllib.request pour envoyer des requêtes HTTP, et json pour manipuler les données JSON.

```python 
import urllib.request
import json
```

### ETAPE 2 : Construire l’URL de la requête
L’utilisateur doit saisir une adresse postale. On va construire l’URL en ajoutant cette adresse au paramètre ```q```.

```python
adresse = input("Entrez une adresse postale : ").replace(' ', '-')
code_postal = input("Entrez le code postal")
url = f'https://api-adresse.data.gouv.fr/search/?q={adresse}&postcode={code_postal}'
```

### ETAPE 3 : Envoyer la requête et récupérer la réponse
```python
    try:
        reponse = urllib.request.urlopen(url)
        data = json.load(reponse)
    except Exception as e:
        print("Erreur lors de la requête :", e)
        data = None
```
> Un bloc `try`, `except` permet de détecter une erreur d'exécution et de réagir en conséquence sans faire planté le programme. Si une exception se déclenche dans le bloc `try`, le programme ne s'arrête pas mais exècute le code situé dans le bloc `except`. Très utile lorsque l'on veut gérer des exceptions que l'on ne peut pas anticiper au préalable. (**Exemple :** Un fichier qui n'existe pas, une url inconnue ...)

### ETAPE 4 : Analyser et afficher les résultats
L’API renvoie une liste de résultats dans le champ features. On récupère le premier résultat (le plus pertinent) et on affiche quelques informations.

```python
if data != None and data['features']:
    feature = data['features'][0]
    properties = feature['properties']
    
    print("Adresse trouvée :", properties['label'])
    print("Code postal :", properties['postcode'])
    print("Ville :", properties['city'])
    print("Latitude :", properties['context'].split(',')[0])
    print("Longitude :", properties['x'], properties['y'])  
else:
    print("Aucun résultat trouvé pour cette adresse.")
```

**QUESTION 1**

Recopier et exécuter le code précédent pour vérifier qu'il fonctionne.

## Activité 2
On s'intéresse cette fois-ci à l'API https://freegeoip.app/json qui permet d'obtenir des informations géographiques sur une adresses IP.

**Question 2**

En vous aidant de l'activité 1 proposer une fonction qui prend une adresse IP en paramètres et qui renvoie la ville associé à cette adresse.

> - L'url se construit de la façon suivante : `https://freegeoip.app/json/ip-a-tester`
> - Interroger l'API à partir de votre navigateur afin de lire comment est construite la réponse JSON.

## Activité 3
On s'intéresse à l'API https://httpbin.org/post. Cette API est un simple service de test qui renvoie ce qu'on lui envoie, idéal pour comprendre comment envoyer des données à l'aide d'une requête **POST**.

### ETAPE 1 : Importer les modules nécessaires
```python
import urllib.request
import json
```

### ETAPE 2 : Préparer les données à envoyer
```python 
donnees = {
    'nom': 'Dupont',
    'age': 25,
    'ville': 'Paris'
}
```

### ETAPE 3 : Convertir les données en JSON
```python
donnees_json = json.dumps(donnees).encode('utf-8')
```

### ETAPE 4 : Construire la requête
```python
url = 'https://httpbin.org/post'
requete = urllib.request.Request(url, data=donnees_json, method='POST')
requete.add_header('Content-Type', 'application/json')
```

### ETAPE 5 : Envoyer la requête et récupérer la réponse
```python
try:
    reponse = urllib.request.urlopen(requete)
    reponse_json = json.load(reponse)
except Exception as e:
    print("Erreur lors de la requête :", e)
``` 

### ETAPE 6 : Afficher la réponse reçue
```python
print(json.dumps(reponse_json, indent=4, ensure_ascii=False))
```