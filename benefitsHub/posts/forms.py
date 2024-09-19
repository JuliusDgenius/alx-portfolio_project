"""
This module defines the post forms for the application.
"""
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired


class MakePostForm(FlaskForm):
    """Class to create a new post"""
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    post_image = FileField('Upload picture', validators=[FileAllowed(['jpg', 'jpeg', 'png', 'gif'])])
    submit = SubmitField('Post')
