from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField 
from wtforms.validators import DataRequired

class MedicationForm(FlaskForm):
    medication = StringField('Medication', validators=[DataRequired()])
    dosage = StringField('Dosage', validators=[DataRequired()])
    submit = SubmitField('Record Dose')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')
    