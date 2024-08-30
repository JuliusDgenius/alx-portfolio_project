from benefitsHub import db, login_manager
from datetime import datetime
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    profile_pic = db.Column(db.String(20), nullable=False, default='default.jpg')
    benefits = db.relationship('Benefit', backref='user', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', {self.profile_pic})"


class Benefit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    description = db.Column(db.String(120), unique=True, nullable=False, default='')
    benefit_image = db.Column(db.String(20), unique=True, nullable=False, default='default.jpg')
    benefit_requirement = db.Column(db.String(120), unique=True, nullable=False, default=None)
    benefit_duration = db.Column(db.Integer, nullable=False, default=None)
    benefit_link = db.Column(db.String(60), nullable=False, default=None)
    benefit_start_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    benefit_end_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    benefit_status = db.Column(db.String(60), nullable=False, default=None)
    benefit_created_by = db.Column(db.String(60), nullable=False, default=None)
    benefit_created_on = db.Column(db.String(60), nullable=False, default=None)
    benefit_updated_by = db.Column(db.String(60), nullable=False, default=None)
    benefit_updated_on = db.Column(db.String(60), nullable=False, default=None)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False, default=None)

    def __repr__(self):
        return f"Benefit('{self.name}', '{self.benefit_duration}',\
                        '{self.benefit_start_date}',\
                        '{self.benefit_end_date}', '{self.benefit_status}',\
                        '{self.benefit_created_by}', '{self.benefit_updated_on}')"