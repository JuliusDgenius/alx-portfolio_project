from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


app = Flask(__name__)

app.config['SECRET_KEY'] = 'fdf898181ba60d610301084df980e442'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///benefitsHub.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

# Import routes
from benefitsHub import routes
