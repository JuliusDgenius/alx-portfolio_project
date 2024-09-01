from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, login_manager


app = Flask(__name__)

app.config['SECRET_KEY'] = 'fdf898181ba60d610301084df980e442'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///benefitsHub.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
login_manager.login_view = 'login' # The name of the route to redirect to if the user is not logged in.
login_manager.login_message_category = 'info'

app.config['UPLOAD_FOLDER'] = 'uploads/'  # Define the upload folder
app.config['ALLOWED_EXTENSIONS'] = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}  # Allowed file extensions
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # Max upload size (16 MB)

# Import routes
from benefitsHub import routes
