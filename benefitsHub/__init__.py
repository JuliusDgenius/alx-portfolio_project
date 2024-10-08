"""Import necessary Flask extensions and modules"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from benefitsHub.config import Config

# Initialize Flask extensions
db = SQLAlchemy()
bcrypt = Bcrypt()
migrate = Migrate()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
email = Mail()

def create_app(app_config=Config):
    """
    Create and configure an instance of the Flask application.
    
    Args:
        app_config: Configuration object for the app (default: Config)
    
    Returns:
        app: Configured Flask application instance
    """
    # Create Flask app instance
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize Flask extensions with the app
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    email.init_app(app)
    migrate.init_app(app, db)

    # Import and register blueprints
    from benefitsHub.users.routes import users
    from benefitsHub.benefits.routes import benefits
    from benefitsHub.posts.routes import posts
    from benefitsHub.main.routes import main
    from benefitsHub.errors.handlers import errors

    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(benefits)
    app.register_blueprint(main)
    app.register_blueprint(errors)

    return app
