#!/bin/env python3
"""
This module defines the models for the application.
"""
from flask import current_app
from benefitsHub import db, login_manager, Serializer
from datetime import datetime
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    """Load a user by their ID"""
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    """User model"""
    # Primary key for the user
    id = db.Column(db.Integer, primary_key=True)
    # Unique username for the user
    username = db.Column(db.String(20), unique=True, nullable=False)
    # Unique email for the user
    email = db.Column(db.String(120), unique=True, nullable=False)
    # Hashed password for the user
    password = db.Column(db.String(60), nullable=False)
    # Profile picture filename for the user
    profile_pic = db.Column(db.String(20), nullable=False,
                            default='default.jpg')
    # Relationship with benefits table
    benefits = db.relationship('Benefit', backref='user', lazy=True)
    # Relationship with posts table
    posts = db.relationship('Post', backref='user', lazy=True)

    def __repr__(self):
        """Return a string representation of the user"""
        return f"User('{self.username}', '{self.email}', {self.profile_pic})"

    def get_reset_token(self, expires=1800):
        """Get a reset token for the user"""
        s = Serializer(current_app.config['SECRET_KEY'], expires)
        return s.dumps({"user_id": self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        """Verify a reset token for the user"""
        s = Serializer(current_app.config['SECRET_KEY'])
        try:    
            user_id = s.loads(token)['user_id']
        except Exception as e:
            print(e)
            return None

        return User.query.get(user_id)


class Benefit(db.Model):
    """Benefit model"""
    # Primary key for the benefit
    id = db.Column(db.Integer, primary_key=True)
    # Name of the benefit
    name = db.Column(db.String(120), unique=True, nullable=False)
    # Description of the benefit
    description = db.Column(db.Text, nullable=False, default='')
    # Image filename for the benefit
    benefit_image = db.Column(db.String(255), nullable=True)
    # Requirements for the benefit
    benefit_requirement = db.Column(db.Text, nullable=True)
    # Link to more information about the benefit
    benefit_link = db.Column(db.String(60), nullable=True)
    # Start date of the benefit
    benefit_start_date = db.Column(db.DateTime, nullable=False,
                                   default=datetime.utcnow)
    # End date of the benefit
    benefit_end_date = db.Column(db.DateTime, nullable=False,
                                 default=datetime.utcnow)
    # Status of the benefit (e.g., Active, Inactive)
    benefit_status = db.Column(db.String(60), nullable=False,
                               default='Active')
    # Username of the user who created the benefit
    benefit_created_by = db.Column(db.String(60), nullable=False, default='')
    # Date and time when the benefit was created
    benefit_created_on = db.Column(db.DateTime, nullable=False,
                                   default=datetime.utcnow)
    # Username of the user who last updated the benefit
    benefit_updated_by = db.Column(db.String(60), nullable=False, default='')
    # Date and time when the benefit was last updated
    benefit_updated_on = db.Column(db.DateTime, nullable=False,
                                   default=datetime.utcnow)
    # Foreign key to the user table
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        """Return a string representation of the benefit"""
        return (f"Benefit('{self.name}', "
                f"'{self.benefit_start_date}', "
                f"'{self.benefit_end_date}', '{self.benefit_status}', "
                f"'{self.benefit_created_by}', "
                f"'{self.benefit_updated_on}')")


class Post(db.Model):
    """Post model"""
    # Primary key for the post
    id = db.Column(db.Integer, primary_key=True)
    # Title of the post
    title = db.Column(db.String(20), unique=True, nullable=False)
    # Content of the post
    content = db.Column(db.Text, unique=True, nullable=False, default='')
    # Date and time when the post was created
    date_posted = db.Column(db.DateTime, nullable=False,
                            default=datetime.utcnow)
    # Username of the author of the post
    author = db.Column(db.String(60), nullable=False, default=None)
    # Foreign key to User model
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),
                        nullable=False)

    def __repr__(self):
        """Return a string representation of the post"""
        return f"Post('{self.title}', '{self.content}', '{self.author}')"
