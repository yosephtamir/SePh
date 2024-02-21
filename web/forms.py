#!/usr/bin/python3.8
"""
Every required forms for the app is included here
"""
from flask_wtf import FlaskForm
from models import storage
from models.user import User
from models.city import City
from models.subcity import SubCity
from models.category import Category
from flask_wtf.file import FileField, FileAllowed
from wtforms import PasswordField, SubmitField, BooleanField, FloatField
from wtforms import StringField, TextAreaField, RadioField, SelectField
from wtforms.validators import Email, EqualTo, ValidationError
from wtforms.validators import DataRequired, Length

class RegistrationForm(FlaskForm):
    """Used for registering a new user"""
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
    password = PasswordField('Password', validators=[DataRequired(),
                                                     Length(min=8, max=128)])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(),
                                                 EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = storage.valCheck("username", value=username.data)
        if user:
            raise ValidationError('That username is taken. \
                                  Please choose a different one.')

    def validate_email(self, email):
        user = storage.valCheck("email", value=email.data)
        if user:
            raise ValidationError('That email is taken. \
                                  Please choose a different one.')
        
    def validate_phonenumber(self, phonenumber):
        user = storage.valCheck("phonenumber", value=phonenumber.data)
        if user:
            raise ValidationError('That email is taken. Please \
                                  choose a different one.')


class LoginForm(FlaskForm):
    """"used for user authentication"""
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Log In')

class CategoryForm(FlaskForm):
    """Used to add category to the app"""
    name = StringField("name")
    submit = SubmitField('Add to Category')

    def validate_name(self, name):
        user = storage.valCheck("name", value=name.data, cls="Category")
        if user:
            raise ValidationError('This category already exists.')

class CityForm(FlaskForm):
    """Used to add city to the app"""
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
    """Used to add subcity to the app"""
    city_name = StringField("City Name", default="Addis Ababa")
    subCity_name = StringField("Sub city name")
    submit = SubmitField('Add to subcity')

    def validate_subCity_name(self, subCity_name):
        subCity = storage.valCheck("subcity", value=subCity_name.data,
                                   cls="SubCity")
        if subCity:
            raise ValidationError('This SubCity already exists.')


class UserProfile(FlaskForm):
    """"This form is used to update a user profile"""
    first_name = StringField('First Name',
                           validators=[Length(min=2, max=20)])
    last_name = StringField('Last Name',
                           validators=[Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[Email()])
    phonenumber = StringField('Phone Number')
    country = StringField('Country',
                           validators=[ Length(min=4, max=20)],
                           default="Ethiopia")
    region = StringField('Region',
                           validators=[Length(max=20)],
                           default="Addis Ababa")
    zone = StringField('Zone',
                           validators=[Length(max=20)])
    wereda = StringField('Wereda',
                           validators=[Length(max=20)])
    idnumb = StringField('ID Number',
                           validators=[Length(min=2, max=128)])
    profilepic = FileField('Update profile Picture',
                           validators=[FileAllowed(['jpg', 'png', 'jpeg',
                                                    'PNG', 'JPEG', 'PNG'])])
    
    password = PasswordField('Password', validators=[DataRequired(),
                                                     Length(min=8, max=128)])

    submit = SubmitField('Update My Profile')

    def validate_email(self, email):
        user = storage.valCheck("email", value=email.data)
        if user and user.email != email.data:
            raise ValidationError('That email is taken.\
                                  Please choose a different one.')
        
    def validate_phonenumber(self, phonenumber):
        user = storage.valCheck("phonenumber", value=phonenumber.data)
        if user:
            if user.phonenumber != phonenumber.data:
                raise ValidationError('That phone number is taken.\
                                      Please choose a different one.')

class PropertyForm(FlaskForm):
    """"This form is used to post a property"""
    citydict = storage.all(City).values()
    subcitydict = storage.all(SubCity).values()
    catagories = storage.all(Category).values()
    citylist = []
    subcitylist = []
    catagorylist = []

    for city in citydict:
        citylist.append((city.city, city.city))
    
    for subcity in subcitydict:
        subcitylist.append((str(subcity.subcity), str(subcity.subcity)))

    for catagory in catagories:
        catagorylist.append((str(catagory.name), str(catagory.name)))


    name = StringField("Name", validators=[DataRequired()])
    price = FloatField("Price", validators=[DataRequired()])
    kare = FloatField("Kare", validators=[DataRequired()])
    category = SelectField("Catagory", choices=catagorylist,
                           validators=[DataRequired()])
    details = StringField("Details", validators=[DataRequired()])
    city = SelectField("City", choices=citylist, validators=[DataRequired()])
    subcity = SelectField("SubCity", choices=subcitylist,
                          validators=[DataRequired()])
    addressline1 = StringField("Address Line 1", validators=[DataRequired()])
    addressline2 = StringField("Address Line 2")
    image1 = FileField('Image 1', validators=[DataRequired(),
                                              FileAllowed(['jpg', 'png',
                                                           'jpeg', 'PNG',
                                                           'JPEG', 'PNG'])])
    image2 = FileField('Image 3', validators=[FileAllowed
                                              (['jpg', 'png', 'jpeg',
                                                'PNG', 'JPEG', 'PNG'])])
    image3 = FileField('Image 3', validators=[FileAllowed
                                              (['jpg', 'png', 'jpeg',
                                                'PNG', 'JPEG', 'PNG'])])

    submit = SubmitField('Post Your Property')

    
    def validate_subcity(self, subcity):
        subcityname = storage.valCheck("subcity", value=subcity.data,
                                       cls="SubCity")
        if subcityname == None:
            raise ValidationError('Subcity does not exist')
        
    def validate_category(self, category):
        categoryname = storage.valCheck("name", value=category.data,
                                        cls="Category")
        if categoryname == None:
            raise ValidationError('Category does not exist')
        

class EditPropertyForm(FlaskForm):
    """"This form is used to post a property"""
    name = StringField("Name", validators=[DataRequired()])
    price = FloatField("Price", validators=[DataRequired()])
    kare = FloatField("Kare", validators=[DataRequired()])
    details = StringField("Details", validators=[DataRequired()])

    submit = SubmitField('Update Your Property')

    
    def validate_name(self, name):
        if name == None or name == "":
            raise ValidationError('Name can not be none')
        
    def validate_price(self, price):
        if price == None or price == "":
            raise ValidationError('price can not be none')
    def validate_kare(self, kare):
        if kare == None or kare == "":
            raise ValidationError('kare can not be none')
    def validate_details(self, details):
        if details == None or details == "":
            raise ValidationError('details can not be none')
        
class MessageForm(FlaskForm):
    """"This form is used to post a property"""
    message = TextAreaField("Message", validators=[DataRequired()])
    submit = SubmitField('Send')