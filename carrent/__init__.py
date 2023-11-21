"""Initiating the flask app"""
from flask import Flask
from urllib.parse import quote_plus
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ac2f1736284e44ba9b19ccdc97e783b9'
password = quote_plus('123456@App')
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://carrent_dev:{password}@localhost/carrent_db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from carrent import routes
