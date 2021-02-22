# P7_GrandPy
-----------------

**Le concept de l'application ?**

Vous donnez des adresses à GrandPy et il vous répond, avec l'adresse, une petite histoire et même le lieu sur sa carte
Vraiment impressionnant ce GrandPy.

**Veux-tu voir le site ?**

[Voici le lien](https://grandpy68.herokuapp.com/)

Je vais te donner quelques phrases pour que tu essayes:
Bonsoir Grandpy, j'espère que tu as passé une belle semaine. Est-ce que tu pourrais m'indiquer l'adresse de la tour eiffel ?
Salut grandpy! Comment s'est passé ta soirée avec Grandma hier soir?

-----------------

**Le site te plaît ?**

Alors suit mes instructions en bas pour avoir le même site.
Autrement à ta libre imagination pour les modifications.

-----------------

**Avez vous déjà l'application Python ?**

Pour ouvrir cette application coder en Python, il vous faudra l'installer.
Rendez-vous sur le [site de Python](https://www.python.org/) pour l'installation.


**Comment lancer l'application ?**

Il vous faut tout d'abord créer un environnement virtuel.
Explication:

Il faut accéder à l'invite de commande:
Dans le champ de recherche du menu Démarrer taper la commande suivante:

-`cmd`
Ceci permet d'accéder a l'invite de commande.

-`pip install virtualenv`
Ceci est l'installation d'un environnement virtuel.

-`virtualenv -p python3 env`
Ceci va vous créer un dossier ''env''.

-`source env/bin/activate`
Ceci active un environnement virtuel.

-----------------

**Installation des différentes exigences**


Ensuite, il vous faudra installer les différentes exigences pour la bonne utilisation du jeu.
Explication :

-`python3 -m pip install -r requirements.txt`
Ceci installera les differentes exigences du jeu.

-----------------

**Goole maps**

Il faudra demander une clé d'api google.
Rendez-vous sur le [site de Google](https://cloud.google.com/) pour avoir votre clé.

Remplacez => os.environ.get('KEY_MAPS') <= par votre mot de passe dans le fichier env.

-----------------

**Lancement de l'application**

-`python app.py`
Ceci vous lancera automatiquement l'application.

