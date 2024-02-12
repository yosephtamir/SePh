from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, FloatField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    first_name = StringField('first_name',
                           validators=[DataRequired(), Length(min=2, max=20)])
    last_name = StringField('last_name',
                           validators=[DataRequired(), Length(min=2, max=20)])
    username = StringField('username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('email',
                        validators=[DataRequired(), Email()])
    phonenumber = StringField('phonenumber',
                           validators=[DataRequired(), Length(min=2, max=128)])
    country = StringField('country',
                           validators=[DataRequired(), Length(min=2, max=128)])
    region = StringField('region',
                           validators=[DataRequired(), Length(min=2, max=128)])
    zone = StringField('zone',
                           validators=[DataRequired(), Length(min=2, max=128)])
    wereda = StringField('wereda',
                           validators=[DataRequired(), Length(min=2, max=128)])
    idnumb = StringField('idnumb',
                           validators=[DataRequired(), Length(min=2, max=128)])
    profilepic = StringField('profilepic',
                           validators=[Length(min=2, max=128)])
    
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=128)])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Log In')