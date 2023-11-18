from flask import Flask
from urllib.parse import quote_plus
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ac2f1736284e44ba9b19ccdc97e783b9'
password = quote_plus('123456@App')
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://carrent_dev:{password}@localhost/carrent_db'
db = SQLAlchemy(app)

from carrent import routes