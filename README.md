# LIVRES API VERSION 1

## Getting Started

### Installation des Dépendances

#### Python  3.10.2
#### pip 21.2.4 from C:\Python\lib\site-packages\pip (python 3.10)

Suivez les instructions suivantes pour installer l'ancienne version de python sur la plateforme [python docs](https://www.python.org/downloads/)

#### Dépendances de PIP

Pour installer les dépendances, exécuter la commande suivante:

```bash ou powershell ou cmd
pip install -r requirements.txt
ou
pip3 install -r requirements.txt
```

Nous passons donc à l'installation de tous les packages se trouvant dans le fichier `requirements.txt`.

##### clé de Dépendances

- [Flask](http://flask.pocoo.org/)  est un petit framework web Python léger, qui fournit des outils et des fonctionnalités utiles qui facilitent la création d’applications web en Python.

- [SQLAlchemy](https://www.sqlalchemy.org/) est un toolkit open source SQL et un mapping objet-relationnel écrit en Python et publié sous licence MIT. SQLAlchemy a opté pour l'utilisation du pattern Data Mapper plutôt que l'active record utilisés par de nombreux autres ORM

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

## Démarrer le serveur

Pour démarrer le serveur sur Linux ou Mac, executez:

```bash
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```
Pour le démarrer sur Windows, executez:

```bash
set FLASK_APP=app.py
set FLASK_ENV=development
flask run
``` 

## API REFERENCE

Getting starter

Base URL: At present this app can only be run locally and is not hosted as a base URL. The backend app is hosted at the default, http://localhost:5000; which is set as a proxy in frontend configuration.

## Type d'erreur
Les erreurs sont renvoyées sous forme d'objet au format Json:
{
    "success":False
    "error": 400
    "message":"Ressource non disponible"
}

L'API vous renvoie 4 types d'erreur:
. 400: Bad request (ressource non disponible)
. 500: Internal server error (Erreur interne du serveur)
. 422: Unprocessable (non traitable)
. 404: Not found (Pas trouvé)

## Endpoints
. ## GET/livres

    GENERAL:
        Cet endpoint retourne la liste des livres et le total de livres. 
    
        
    EXEMPLE: curl GET 'http://127.0.0.1:5000/livres'
```
{
    "livres": [
        {
            "Catégorie livre": 5,
            "auteur": "Diallo",
            "date_publication": "15-02-2022",
            "editeur": "x",
            "id": 4,
            "isbn": "X1950",
            "titre": "Montagne"
        },
        {
            "Catégorie livre": 4,
            "auteur": "Mamadou",
            "date_publication": "15-02-2022",
            "editeur": "cxcx",
            "id": 5,
            "isbn": "X195",
            "titre": "Montagne neige"
        },
        {
            "Catégorie livre": 2,
            "auteur": "F2B",
            "date_publication": "16-02-2022",
            "editeur": "x",
            "id": 7,
            "isbn": "X10",
            "titre": "De dans de"
        },
        {
            "Catégorie livre": 5,
            "auteur": "Jack",
            "date_publication": "16-02-2022",
            "editeur": "JM",
            "id": 8,
            "isbn": "X1000",
            "titre": "007"
        },
        {
            "Catégorie livre": 2,
            "auteur": "Mosty",
            "date_publication": "20-02-2022",
            "editeur": "Furax",
            "id": 6,
            "isbn": "X190",
            "titre": "Faut danser"
        }
    ],
    "total_livres": 5
}
```

.##GET/livres(id_livre)
  GENERAL:
  Cet endpoint permet de récupérer les informations d'un livre particulier s'il existe par le biais de l'ID.

    EXEMPLE: http://localhost:5000/livres/6
```
{
    "Catégorie livre": 2,
    "auteur": "Mosty",
    "date_publication": "20-02-2022",
    "editeur": "Furax",
    "id": 6,
    "isbn": "X190",
    "titre": "Faut danser"
}
```


. ## DELETE/livres(id_livre)

    GENERAL:
        Supprimer un element si l'ID existe. Retourne l'ID du livre supprimé, la valeur du succès et le nouveau total.

        EXEMPLE: curl -X DELETE http://localhost:5000/livres/4
```
{
    "delete successfully": 4,
    "success": true,
    "total_livres": 4
}
```

. ##PATCH/livres(id_livre)
  GENERAL:
  Cet endpoint permet de mettre à jour, le titre, l'auteur, et l'éditeur du livre.
  Il retourne un livre mis à jour.

  EXEMPLE.....Avec Patch
  ``` curl -X PATCH http://localhost:5000/livres/6 -H "Content-Type:application/json" -d '{"categorie_id": 2,"auteur": "XXXX","date_publication": "20-02-2022","editeur": "Vie","titre": "Faut danser"}'
  ```
  ```
{
    "Livre": {
        "Catégorie livre": 2,
        "auteur": "XXXX",
        "date_publication": "20-02-2022",
        "editeur": "Vie",
        "id": 6,
        "isbn": "X190",
        "titre": "Faut danser"
    },
    "success modify": true
}
    ```

. ## GET/categories

    GENERAL:
        Cet endpoint retourne la liste des categories de livres et le total des categories disponibles. 
    
        
    EXEMPLE: curl http://localhost:5000/categories

        {
    "categories": [
        {
            "id": 2,
            "libelle_categorie": "Physiques"
        },
        {
            "id": 4,
            "libelle_categorie": "Sport"
        },
        {
            "id": 5,
            "libelle_categorie": "Langages de programmation"
        },
        {
            "id": 1,
            "libelle_categorie": "Sciences"
        },
        {
            "id": 6,
            "libelle_categorie": "Maths"
        },
        {
            "id": 7,
            "libelle_categorie": "Sciences Naturelles"
        }
    ],
    "total_categories": 6
}
```

.##GET/categories(categorie_id)
  GENERAL:
  Cet endpoint permet de récupérer les informations d'une categorie si elle existe par le biais de l'ID.

    EXEMPLE: http://localhost:5000/categories/6
```
   {
        "id": 2,
        "libelle_categorie": "Physiques"
    }
```

. ## DELETE/categories (categories_id)
    GENERAL:
        Supprimer un element si l'ID existe. Retourne l'ID da la catégorie supprimé, la valeur du succès et le nouveau total.

        EXEMPLE: curl -X DELETE http://localhost:5000/categories/7
```
   {
        "delete successfully": 7,
        "success": true,
        "total_categories": 3
    }
```

. ##PATCH/categories(categorie_id)
  GENERAL:
  Cet endpoint permet de mettre à jour le libelle ou le nom de la categorie.
  Il retourne une nouvelle categorie avec la nouvelle valeur.

  EXEMPLE.....Avec Patch
  ``` curl -X PATCH 'http://localhost:5000/categories/2' -H "Content-Type:application/json" -d '{"libelle_categorie": "Maths"}'
  ```
  ```
   {
        "categorie": {
            "id": 2,
            "libelle_categorie": "Maths"
        },
        "success modify": true
    }

.##GET/categories(categorie_id)/livres
  GENERAL:
  Cet endpoint permet de lister les livres appartenant à une categorie donnée ainsi que le total de livres contenu dans cette dernière

    EXEMPLE: http://localhost:5000/categories/5/livres
```
{
    "livres": [
        {
            "Catégorie livre": 5,
            "auteur": "Diallo",
            "date_publication": "15-02-2022",
            "editeur": "x",
            "id": 4,
            "isbn": "X1950",
            "titre": "Montagne"
        },
        {
            "Catégorie livre": 5,
            "auteur": "Jack",
            "date_publication": "16-02-2022",
            "editeur": "JM",
            "id": 8,
            "isbn": "X1000",
            "titre": "007"
        }
    ],
    "total_livres": 2
}
```

