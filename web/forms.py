from flask_wtf import FlaskForm
from models import storage
from models.user import User
from wtforms import StringField, PasswordField, SubmitField, BooleanField, FloatField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError


class RegistrationForm(FlaskForm):
    first_name = StringField('First Name',
                           validators=[DataRequired(), Length(min=2, max=20)])
    last_name = StringField('Last Name',
                           validators=[DataRequired(), Length(min=2, max=20)])
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    phonenumber = StringField('Phone Number',
                           validators=[DataRequired(), Length(min=2, max=128)])
    """country = StringField('Country',
                           validators=[DataRequired(), Length(min=2, max=128)])
    region = StringField('Region',
                           validators=[DataRequired(), Length(min=2, max=128)])
    zone = StringField('Zone',
                           validators=[DataRequired(), Length(min=2, max=128)])
    wereda = StringField('Wereda',
                           validators=[DataRequired(), Length(min=2, max=128)])
    idnumb = StringField('ID Number',
                           validators=[DataRequired(), Length(min=2, max=128)])
    profilepic = StringField('Profile Picture',
                           validators=[Length(min=2, max=128)])"""
    
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=128)])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = storage.valCheck("username", value=username.data)
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        user = storage.valCheck("email", value=email.data)
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')
        
    def validate_phonenumber(self, phonenumber):
        user = storage.valCheck("phonenumber", value=phonenumber.data)
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Log In')

class CategoryForm(FlaskForm):
    name = StringField("name")
    submit = SubmitField('Add to Category')

    def validate_name(self, name):
        user = storage.valCheck("name", value=name.data, cls="Category")
        if user:
            raise ValidationError('This category already exists.')
