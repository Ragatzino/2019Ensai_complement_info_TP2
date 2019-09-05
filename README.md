# Complément informatique, 2A, TP2

## Objectif du TP

Apprendre à communiquer avec un webservice (récupération et envoi de données) avec la bibliothèque **requests** ainsi que créer son propre webservice avec la bibliothèque **Flask**

Notions principales abordées :

- Webservice (API)
- Client-serveur

Notions secondaires :

- injection de code
- Git
- webscrapping 

## Communication Client-Serveur, webservice REST

### 0. Récupérer le code du TP

TODO 

### 1. Côté Client - Appeler un webservice


#### 1.1 Préparation
Ouvrez PyCharm ou VScode et ouvrez le dossier squelette-tp3-client :

    - PyCharm :  File > Open > cherchez le dossier
    - VScode : File > Open Foleder > cherchez le dossier


Dans cette première partie, nous allons utiliser les webservices du site open-data de Rennes : https://data.rennesmetropole.fr/explore/ 
 
Tous les connections sortantes de l'Ensai passe par un proxy. Ainsi pour le webservice que vous allez contacter, toutes les connections sont faites depuis la même source. Si rien n'est fait , le quota de requêtes pour une même source va être rapidement dépassé. Pour éviter cela, vous allez devoir vous créer un compte que le site qui vous founira une clef pour que le service arrivent à vous différencier et ainsi ne plus avoir un quota pour l'école, mais un quota par élèves.

Pour vous créer un compte allez sur le site : https://data.rennesmetropole.fr/explore. Puis en haut à droite cliquez sur Inscription et suivez les étapes. Une fois cela fait connectez-vous, allez dans votre compte (cliquez sur votre nom), puis "clé d'API". Générez une clé et donnez lui le nom que vous voulez. Copiez-collez cette clé dans le fichier properties.py.
 
#### 1.2 Insomnia et les requêtes à la main
 
Avant de lancer l’exemple, ouvrez le fichier exemple.py. Dans cet exemple vous récupérez les informations depuis une url ( https://
data.rennesmetropole.fr/….. ). Pour consulter ce que renvoie cette url, vous allez utiliser Insomnia.

Lancez Insomnia depuis le menu démarrer (Menu démarrer / Informatique / Insomnia). Allez dans le menu application/préférence pour configurer le proxy. Cliquez sur la checkbox Enable Proxy et saisissez dans les champs HTTP Proxy et HTTPS Proxy : 

> http:// pxcache-02.ensai.fr:3128

Dans Insomnia, cliquez sur le bouton + à gauche > New Requests. Dans la popin qui s’ouvre, mettez comme nom Prêts de DVD puis appuyez sur Create (vous avez un menu déroulant avec GET sélectionné, laissez cette méthode).

En haut, dans le champ texte à côté de GET, collez l’url ( https://data.rennesmetropole.fr/….. ) qui est présente dans l’exemple puis appuyez sur SEND (pensez à mettre mon api_key dans l'url)

Vous obtenez dans la fenêtre de droite le résultat de la requête.

#### 1.3 Le requêtage avec pyhton
 
Maintenant nous allons lancer la programme, il se base sur 2 librairies :
- requests (http://docs.python-requests.org/) qui permet d’appeler l’API
- tabulate (https://pypi.org/project/tabulate/) qui facilite l’affichage des tableaux


Si cela s'avère nécessaire, installez ces dépendances (présentes dans le fichiers requirements.txt)

> pip install -r requirements.txt --user --proxy http://pxcache-02.ensai.fr:3128

Lancez l’exemple. Vous devriez voir s’afficher la liste des films star wars qui ont été empruntés. 

De façon similaire, vous allez maintenant appeler une autre url pour afficher les arrêts de bus de Bruz accessibles aux personnes à mobilité réduite.

Avec un navigateur, allez sur le site https://data.rennesmetropole.fr/page/home/. Puis dans l’onglet Mes Données, allez sur Données géographiques du réseau STAR : arrêts physiques et enfin sur l’onglet API. En bas de cette page, vous avez l’url pour récupérer les résultats de l’appel. Elle est construite en fonction des paramètres que vous choisissez sur la page. Cliquez dans le menu à gauche sur Bruz (sous Commune (nom)), vous devez constatez que dans l’url un nouveau paramètre a été ajouté : refine.nomcommune=Bruz

Ainsi nous ne récupérons que les arrêts de bus situés à Bruz Vous avez un champs texte sur la page appelé rows, c’est le nombre de résultats de la requête. Par défaut il vaut 10. Saisissez 100 pour récupérer l’ensemble des résultats et cliquez sur le bouton Envoyez en bas. Vous devez constater que dans l’url un nouveau paramètre a été ajouté : rows=100

Maintenant cliquez sur le lien, un nouvel onglet va s’ouvrir. Récupérez l’url et saisissez là dans Insomnia comme vous l’avez fait précédemment (Cliquez sur +, sur New Request …). Consultez les données qui sont renvoyées par l’url.

Nous voulons récupérer les coordonnées (latitude et longitude) des arrêts de bus accessibles aux personnes à mobilité réduite (pmr). Affichez un tableau listant les coordonnées des arrêts de bus accessibles aux personnes à mobilité réduite avec pour colonnes latitude et longitude. Nous nous contentons d’afficher les coordonnées dans le cadre de ce TP mais nous pourrions les afficher sur une carte avec OpenStreetMap par exemple.  (le filtre est disponible dans le partie1.py)


### 2. Côté Serveur - Construire son API

##### Constuire son API

Ouvrez dans une autre fenêtre le code contenu dans squelette-tp2-serveur.
- PyCharm : File > Open > New Window
- VS code : File > New Windows > Open Foler 

Normalement aucune dépendance n'est nécessaire, mais si besoin vous pouvez les installer via 

> pip install -r requirements.txt --user --proxy http://pxcache-02.ensai.fr:3128
 
Flask permet de créer des webservices (http://flask.pocoo.org)
Lancez l’exemple. Il contient une serveur qui répond sur 2 urls : /films et /film 

Sur Insomnia allez dans le menu Application > Preferences et décochez la case Enable Proxy. Ajoutez une nouvelle requête GET (New Request) et interrogez l’url http://localhost:5000/films
Vous devez voir s’afficher la liste des 3 films que l’on retrouve dans files/movies.csv.

Si vous regardez le code, vous avez une méthode movieList qui supporte la méthode GET et qui retourne la liste des films. Pour récupérer la liste, elle utilise une DAO.

> Dans le cas présent, c'est un fichier qui est utilié pour stockez les données, et pas une base. Pourtant il y a toujours intérêt à utiliser une DAO entre le système de persistance et le métier de mon application (qui est ici très pauvre)

Nous allons maintenant ajouter un film. Sur Insomnia, ajoutez une nouvelle requête (New Request) mais dans la popin au lieu de laisser GET, remplacer par POST, une nouvelle popin va s’afficher avec écrit No Body. Remplacez par
JSON. L’url que l’on va utiliser est http://localhost:5000/film. Dans la fenêtre de gauche (sous JSON), écrivez :

```js
{
  "title": "Mon film préféré"
}
```

Vous pouvez remplacer Mon film préféré par le film que vous souhaitez. Une fois que vous avez exécuté cette appel, appelez à nouveau l’url http://localhost:5000/films en GET et constatez que votre film a été ajouté à la liste.

Si vous regardez le code vous verrez une méthode addMovie qui ajoute le film reçu à la liste. Cette métode fait également appel à une DAO pour l'ajouter du film dans le fichier.

#### Injection d'information

Avant d'aller plus loin dans insomnia, faites une nouvelle requête d'ajout avec le json suivant : 

```js
{
  "title": "Injection via Json; ou comment apprendre vérifier ses inputs "
}
```

Ensuite lancez la requête pour récupérer les films. Essayez de comprendre ce qu'il s'est passé. 


> Pour les correcteurs : ici le but c'est de leur montrer encore une fois le principe d'injection de code. Alors certes on ne va pas faire exécuter du code mais seulement ajouer plus de données que prévu. Dans la DAO les caractères spécifique du CSV ne sont échappés donc on peut "facilement" injecter des données. Je suis sûr qu'en rajoutant des \n on peut également ajouer plusieurs lignes à la fois. Le but c'est les sensibiliser sur le fait que ce qui vient du monde extérieur est potentiellement dangereux. Et qu'il vaut mieux utiliser des outils spécifiques qui vont s'occuper de vérifier nos données et de les insérer que de vouloir tout faire à la main. 

Maintenant que vous avez compris comment fonctionnait le serveur, vous allez ajouter voq propreq méthodeq pour gérer une liste de joueurs qui auront un pseudonyme et un score. Créez les méthodes GET (/joueurs) et POST (/joueur) et testez les appels avec Insomnia.
Pour gagner du temps vous n'allez pas stockez vos joueurs dans des fichiers n'y créer d'objet joueurs, mais uniquement manipuler une liste de dictionnaires python représentant les joueurs.

### 3. Communication Client/Serveur

Dans la première fenêtre de votre IDE qui vous avez ouvert (celle utilisée pour la première partie), créez un programme qui ajoute une liste de joueurs (en appelant la méthode POST de votre serveur) et qui ensuite affiche les 3 premiers (en utilisant la méthode GET pour récupérer la liste)

Note : vous pouvez modifier votre méthode POST pour qu’elle prenne un tableau comme paramètre

### 4. Un peu de webscraping

Nous allons récupérer directement du contenu disponible sur le web. Choisissez une page  wikipedia et affichez le contenu de la balise h1 (le titre de la page). 

Le contenu que vous allez récupérer sera du html, pour extraire le contenu de la balise h1, vous pouvez utiliser la libraire lxml. Pour cette dernière partie, vous allez devoir regarder la documnetation de la bibliothèque par vous même.

## 5. Bonus

Commencez a regarder l'api foursquare et récupérez des données de manière analogue a la partie client de ce tp :) . 
