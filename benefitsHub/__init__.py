from flask import Flask
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, login_manager
from flask_mail import Mail
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from benefitsHub.config import Config

load_dotenv() # Load environment variables from .env


db = SQLAlchemy()
bcrypt = Bcrypt()
migrate = Migrate()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
migrate
email = Mail()


def create_app(app_config=Config):
	app = Flask(__name__)
	app.config.from_object(Config)

	db.init_app(app)
	bcrypt.init_app(app)
	login_manager.init_app(app)
	email.init_app(app)
	migrate.init_app(app, db)

	# Import routes
	from benefitsHub.users.routes import users
	from benefitsHub.benefits.routes import benefits
	from benefitsHub.posts.routes import posts
	from benefitsHub.main.routes import main
	app.register_blueprint(users)
	app.register_blueprint(posts)
	app.register_blueprint(benefits)
	app.register_blueprint(main)

	return app