from flask import Flask
from dotenv import load_dotenv
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, login_manager
from flask_mail import Mail
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer


app = Flask(__name__)
load_dotenv() # Load environment variables from .env
app.config['SECRET_KEY'] = 'fdf898181ba60d610301084df980e442'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///benefitsHub.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
login_manager.login_view = 'login' # The name of the route to redirect to if the user is not logged in.
login_manager.login_message_category = 'info'
# Handle file upload
app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, 'uploaded_images')  # Define the upload folder
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}  # Allowed file extensions
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # Max upload size (16 MB)
# Ensure the upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
# Handle sending emails
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')
print(app.config['MAIL_USERNAME'])
print(app.config['MAIL_PASSWORD'])

email = Mail(app)

# Import routes
from benefitsHub import routes
