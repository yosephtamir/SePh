from flask_wtf import FlaskForm
from models import storage
from models.user import User
from wtforms import FileField
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

class CityForm(FlaskForm):
    city = StringField("City", validators=[DataRequired()])
    submit = SubmitField('Add to city')

    def validate_city(self, city):
        cityname = storage.valCheck("city", value=city.data, cls="City")
        if cityname:
            raise ValidationError('This City already exists.')
        if city.data is None:
            raise ValidationError('City Cannot be Null.')
        if city.data == "":
            raise ValidationError('City Cannot be Null.')
        
class SubCityForm(FlaskForm):
    city_name = StringField("City Name", default="Addis Ababa")
    subCity_name = StringField("Sub city name")
    submit = SubmitField('Add to subcity')

    def validate_subCity_name(self, subCity_name):
        subCity = storage.valCheck("subcity", value=subCity_name.data, cls="SubCity")
        if subCity:
            raise ValidationError('This SubCity already exists.')


class UserProfile(FlaskForm):
    first_name = StringField('First Name',
                           validators=[Length(min=2, max=20)])
    last_name = StringField('Last Name',
                           validators=[Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[Email()])
    phonenumber = StringField('Phone Number')
    country = StringField('Country',
                           validators=[ Length(min=8, max=20)], default="Ethiopia")
    region = StringField('Region',
                           validators=[Length(max=20)], default="Addis Ababa")
    zone = StringField('Zone',
                           validators=[Length(max=20)])
    wereda = StringField('Wereda',
                           validators=[Length(max=20)])
    idnumb = StringField('ID Number',
                           validators=[Length(min=2, max=128)])
    profilepic = StringField('Profile Picture',
                           validators=[Length(max=128)], default="profile.png")
    
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=128)])

    submit = SubmitField('Update My Profile')

    def validate_email(self, email):
        user = storage.valCheck("email", value=email.data)
        if user and user.email != email.data:
            print(user.email)
            print(email.data)
            print(user.email == email.data)
            raise ValidationError('That email is taken. Please choose a different one.')
        
    def validate_phonenumber(self, phonenumber):
        user = storage.valCheck("phonenumber", value=phonenumber.data)
        if user and user.phonenumber is not phonenumber.data:
            raise ValidationError('That phone number is taken. Please choose a different one.')

class PropertyForm(FlaskForm):
    name = StringField("Name", default="Addis Ababa")
    price = FloatField("Price", validators=[DataRequired()])
    kare = FloatField("Kare", validators=[DataRequired()])
    details = StringField("Details", validators=[DataRequired()])
    city = StringField("City", default="Addis Ababa")
    subcity = StringField("SubCity")
    category = StringField("Category")
    addressline1 = StringField("Address Line 2")
    addressline2 = StringField("Address Line 2")
    image1 = StringField("Image 1", validators=[DataRequired()])
    image2 = StringField("Image 2")
    image3 = StringField("Image 3")

    submit = SubmitField('Post Your Property')

    
    def validate_subcity(self, subcity):
        subcityname = storage.valCheck("subcity", value=subcity.data, cls="SubCity")
        if subcityname == None:
            raise ValidationError('Subcity does not exist')
        
    def validate_category(self, category):
        categoryname = storage.valCheck("name", value=category.data, cls="Category")
        if categoryname == None:
            raise ValidationError('Category does not exist')