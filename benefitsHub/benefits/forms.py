"""
This module defines the forms for the application.
"""
from wtforms import StringField, SubmitField, DateField, SelectField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed


class BenefitForm(FlaskForm):
    """Class to create a new benefit"""
    name = StringField('Name', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    benefit_image = FileField('Benefit Image',
                              validators=[FileAllowed(['jpg',
                                                       'jpeg', 'png'])])
    benefit_requirement = StringField('Benefit Requirement',
                                      validators=[DataRequired()])
    benefit_link = StringField('Benefit Link', validators=[DataRequired()])
    benefit_start_date = DateField('Benefit Start Date',
                                   validators=[DataRequired()],
                                   format='%Y-%m-%d')
    benefit_end_date = DateField('Benefit End Date',
                                 validators=[DataRequired()],
                                 format='%Y-%m-%d')
    benefit_status = SelectField('Benefit Status',
                                 choices=[('active', 'Active'),
                                          ('inactive', 'Inactive')],
                                 validators=[DataRequired()])
    benefit_created_by = StringField('Benefit Created By',
                                     validators=[DataRequired()])
    benefit_updated_on = DateField('Benefit Updated On',
                                   validators=[DataRequired()],
                                   format='%Y-%m-%d')

    submit = SubmitField('Create Benefit')
