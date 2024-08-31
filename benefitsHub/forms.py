from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import BooleanField, StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from benefitsHub.models.base_model import User

class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Login')

class UpdateAccountForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    update_picture = FileField('Update profile picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken. Please choose a different one.')


class BenefitForm(FlaskForm):
    """Class to create a new benefit"""
    name = StringField('Name', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    benefit_image = FileField('Benefit Image', validators=[FileAllowed(['jpg', 'png'])])
    benefit_requirement = StringField('Benefit Requirement', validators=[DataRequired()])
    benefit_duration = StringField('Benefit Duration', validators=[DataRequired()])
    benefit_link = StringField('Benefit Link', validators=[DataRequired()])
    benefit_start_date = StringField('Benefit Start Date', validators=[DataRequired()])
    benefit_end_date = StringField('Benefit End Date', validators=[DataRequired()])
    benefit_status = StringField('Benefit Status', validators=[DataRequired()])
    benefit_created_by = StringField('Benefit Created By', validators=[DataRequired()])
    benefit_updated_on = StringField('Benefit Updated On', validators=[DataRequired()])

    submit = SubmitField('Create Benefit')


class MakePostForm(FlaskForm):
    """Class to create a new post"""
    title = StringField('Title', validators=[DataRequired()])
    content = StringField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')