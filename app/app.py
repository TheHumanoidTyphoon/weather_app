from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, static_url_path='/static/')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
db = SQLAlchemy(app)
app.config['SECRET_KEY'] = 'secret_key'

from app.routes import *
