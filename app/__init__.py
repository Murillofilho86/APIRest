from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restless import APIManager


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/storage.db'
db = SQLAlchemy(app)

'''
#Classe para criar tabela usuarios

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))

db.create_all()
'''

#Gerenciado da API 	(app,          banco de dados)
manager = APIManager(app, flask_sqlalchemy_db=db)