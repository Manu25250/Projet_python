from distutils.log import error
from enum import unique
import os
from flask_migrate import Migrate
from flask import Flask, jsonify, redirect, render_template, request, url_for, abort
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)


password = os.getenv("pswdd")
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://ynnxkouchpodtj:60e2fd05c343e9eca907d0577d1d051aafb992a09f1f0d52d9fcbc3ee9464d5d@ec2-35-175-68-90.compute-1.amazonaws.com:5432/d71oaai88b209i'
app.config['SQLACHELMY_TRACK_MODIFICATIONS'] = False
#postgresql://postgres:{}@localhost:5432/biblio'.format(password)
db = SQLAlchemy(app)

#CORS(app) 

#CORS(app, resources={r"/api/*": {"origin": "*"}})   #Préciser le domaine authoriser à interroger une api

migrate = Migrate(app,db)

# Theses classes allowed you to mapp database table with SQLAlchemy
class Categorie(db.Model):
    __tablename__ = "categories"
    id_cat = db.Column(db.Integer, primary_key=True)
    libelle_categorie = db.Column(db.String(100), nullable=False)
    categorie = db.relationship('Livre', backref='categories',lazy=True)

    def __init__(self, libelle_categorie):
        self.libelle_categorie = libelle_categorie

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def format(self):
        return {
            'id': self.id_cat,
            'libelle_categorie': self.libelle_categorie,
        }
      

class Livre(db.Model):
    __tablename__ = "livres"
    id = db.Column(db.Integer, primary_key=True)
    isbn = db.Column(db.String(25), unique=True, nullable=False)
    titre = db.Column(db.String(150), nullable=False)
    date_publication = db.Column(db.String(10), nullable=False)
    auteur = db.Column(db.String(100), nullable=False)
    editeur = db.Column(db.String(100), nullable=False)
    categorie_id = db.Column(db.Integer,db.ForeignKey('categories.id_cat'), nullable=False)

    def __init__(self, isbn,titre,date_publication,auteur,editeur,categorie_id):
        self.isbn = isbn
        self.titre = titre
        self.date_publication = date_publication
        self.auteur = auteur
        self.editeur = editeur
        self.categorie_id = categorie_id

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'isbn': self.isbn,
            'titre': self.titre,
            'date_publication': self.date_publication,
            'auteur': self.auteur,
            'editeur': self.editeur,
            'Catégorie livre' : self.categorie_id,
        }
        
db.create_all()

def boucle(request):
    items = [item.format() for item in request]
    return items


#This route get all list of categories

@app.route('/categories', methods=['GET'])
def get_categories():
    try:
        categories = Categorie.query.all()
        categories = boucle(categories)
        return jsonify({
                'categories': categories,
                'total_categories': len(categories)
                })
    except:
        abort(400)

# We use this route to get one item of categorie you select with id 

@app.route('/categories/<int:id>', methods=['GET'])
def get_categorie(id):
    categorie = Categorie.query.get(id)
    if categorie is None:
        abort(404)
    else:
        return categorie.format()
   

# We use this route to delete one item of categorie 

@app.route('/categories/<int:id>', methods=['DELETE'])
def del_categorie(id):
    
    categorie = Categorie.query.get(id)
    if categorie is None:
        abort(404)    
    categorie.delete()
    categories = Categorie.query.all()
    categories = boucle(categories)
    return jsonify({
        'success': True,
        'delete successfully': id,
        'total_categories': len(categories)
    })



# We use this route to update one item of categorie 

@app.route('/categories/<int:id>', methods=['PATCH'])
def update_categories(id):
    query = Categorie.query.get(id)
    if query is None:
        abort(404)
    try:
        request_data = request.get_json()
        if 'libelle_categorie' in request_data:
            query.libelle_categorie = request_data['libelle_categorie']
        else:
            abort(error)
        query.update()
        return jsonify({
            'success modify': True,
            'categorie': query.format(),
        })
    except:
        abort(400)
    finally:
        db.session.close()

#This route get all list of livres

@app.route('/livres', methods=['GET'])
def get_livres():
    try:
        livres = Livre.query.all()
        livres = boucle(livres)
        return jsonify({
                'livres': livres,
                'total_livres': len(livres)
                })
    except:
        abort(400)

# We use this route to get one item of livre you select with id 

@app.route('/livres/<int:id>', methods=['GET'])
def get_livre(id):
    livre = Livre.query.get(id)
    if livre is None:
        abort(404)
    else:
        return livre.format()

# We use this path or route to delete one item of livre 

@app.route('/livres/<int:id>', methods=['DELETE'])
def del_livre(id):
    livre = Livre.query.get(id)    
    if livre is None:
        abort(404)
    else:
        livre.delete()
    livres = Livre.query.all()
    livres = boucle(livres)
    return jsonify({
        'success': True,
        'delete successfully': id,
        'total_livres': len(livres)
    })

# We use this path or route to update one item of livre 

@app.route('/livres/<int:id>', methods=['PATCH'])
def update_livres(id):
    list={'titre','date_publication','auteur','editeur','categorie_id'}
    query = Livre.query.get(id)
    if query is None:
        abort(404)
    try:
        request_data = request.get_json()
        query.titre = request_data['titre']
        query.date_publication = request_data['date_publication']
        query.auteur = request_data['auteur']
        query.editeur = request_data['editeur']
        query.categorie_id = request_data['categorie_id']
        if(request_data==query):
            abort(error)
        query.update()
        return jsonify({
            'success modify': True,
            'Livre': query.format(),
        })
    except:
        abort(400)
    finally:
        db.session.close()
 
#This route get all list of livres of one categorie

@app.route('/categories/<int:id>/livres', methods=['GET'])
def get_categorie_livres(id):
    livres = Categorie.query.get(id)
    if livres is None:
        abort(404)
    try:
        livres = Livre.query.filter(Livre.categorie_id==id).all()
        #livres = Livre.query.filter_by(categorie_id=id)   !!!Différence entre filter et filter_by!!!
        livres = boucle(livres)
        return jsonify({
                'livres': livres,
                'total_livres': len(livres)
                })
    except:
        abort(400)
    
@app.errorhandler(404)
def not_found(error):
    return (jsonify({'success': False, 'error': 404,
            'message': 'Not found'}), 404)


@app.errorhandler(400)
def error_client(error):
    return (jsonify({'success': False, 'error': 400,
            'message': 'Bad request'}), 400)

@app.errorhandler(500)
def server_error(error):
    return (jsonify({'success': False, 'error': 500,
            'message': 'internal server error'}), 500)

@app.errorhandler(405)
def server_error(error):
    return (jsonify({'success': False, 'error': 405,
            'message': 'method not allowed'}), 405)
