#!/usr/bin/python3
""" Starts a Flash Web Application """
import os
from web.tools import Tools
from PIL import Image
from datetime import datetime
from web import app, bcrypt, login_manager
from web.forms import RegistrationForm, CategoryForm, LoginForm, UserProfile
from web.forms import CityForm, SubCityForm, PropertyForm
from flask import render_template, redirect, url_for, flash, request
from models.user import User
from models.category import Category
from models.property import Property
from models.city import City
from models.subcity import SubCity
from models.place import Place
from models.propertyimage import PropertyImage
from models import storage
from flask_login import login_user, current_user, logout_user, login_required

# app.jinja_env.trim_blocks = True
# app.jinja_env.lstrip_blocks = True

"""login_manager.login_message_category = 'info'"""

def save_picture(picturefile, tobeposted):
    print("here we are")
    timeposted = str(Tools.timestring(datetime.utcnow()))
    _, fileext = os.path.splitext(picturefile.filename)
    picturename = timeposted + fileext
    directory = os.path.join(app.root_path,
                                   f'static/images/{current_user.username}/profilepics')

    if tobeposted == "profilepic":
        directory = f'{app.root_path}/static/images/{current_user.username}/profilepics'
        picturepath = os.path.join(directory,
                                   picturename)
        if not os.path.exists(directory):
            os.makedirs(directory)
    elif tobeposted == "property":
        directory = f'{app.root_path}/static/images/{current_user.username}/property'
        picturepath = os.path.join(directory,
                                   picturename)
        if not os.path.exists(directory):
            os.makedirs(directory)
    else:
        directory = f'{app.root_path}/static/images/{current_user.username}/others'
        picturepath = os.path.join(directory,
                                   picturename)
        if not os.path.exists(directory):
            os.makedirs(directory)
    resValue = (300, 300)
    image = Image.open(picturefile)
    image.resize(resValue)
    image.save(picturepath)

    return picturename



@app.teardown_appcontext
def close_db(error):
    """ Remove the current SQLAlchemy Session """
    storage.close()

@app.route('/', strict_slashes=False)
@app.route('/home', strict_slashes=False)
def home():
    properties = storage.countablefetch(Property).values()
    properties = sorted(properties, key=lambda k: k.updated_at, reverse=True)

    return render_template('seph.html',
                           properties=properties, title = 'Home')

@app.route('/property', strict_slashes=False)
@app.route('/property/<id>', strict_slashes=False)
def property(id=""):
    """ displays a HTML page with a list of cities by states """
    properties = storage.countablefetch(Property).values()
    properties = sorted(properties, key=lambda k: k.name)



    return render_template('seph.html',
                           properties=properties, title = 'Property')
@app.route('/category', strict_slashes=False, methods=["GET", "POST"])
def category():
    form = CategoryForm()
    if form.validate_on_submit():
        if form.name.data:
            category = Category(name=form.name.data)
            storage.new(category)
            storage.save()
            flash(f'{category.name} Successfully Added', 'success')
    return render_template('category.html', form=form, title='Category')

@app.route('/city', strict_slashes=False, methods=["GET", "POST"])
def city():
    form = CityForm()
    if form.validate_on_submit():
        city = City(city=form.city.data)
        storage.new(city)
        storage.save()
        flash(f'{city.city} Successfully Added', 'success')
    return render_template('city.html', form=form, title='City')

@app.route('/subcity', strict_slashes=False, methods=["GET", "POST"])
def subcity():
    form = SubCityForm()
    if form.validate_on_submit():
        cityname = storage.valCheck("city", value=form.city_name.data, cls="City")
        subcity = SubCity(subcity=form.subCity_name.data, cityid=cityname.id)
        storage.new(subcity)
        storage.save()
        flash(f'{subcity.subcity} Successfully Added', 'success')
    return render_template('subcity.html', form=form, title='Sub City')

@app.route('/register', strict_slashes=False, methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(first_name=form.first_name.data, last_name=form.last_name.data,
            username=form.username.data, email=form.email.data,
            phonenumber=form.phonenumber.data,
            country="country", region="region",
            zone="zone", wereda="wereda",
            idnumb="id number", profilepic="default.png",
            password=hashed_password)
        storage.new(user)
        storage.save()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form, title='Register')

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = storage.valCheck("email", value=form.email.data)
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            #next_page = request.args.get('next')
            """redirect(next_page) if next_page else """ 
            return redirect(url_for('register')) 
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/myprofile")
@login_required
def myprofile():
    return render_template('myprofile.html', title='My Profile')

@app.route("/editprofile", methods=['GET', 'POST'])
@login_required
def editprofile():
    form = UserProfile()
    if form.validate_on_submit():
        if bcrypt.check_password_hash(current_user.password, form.password.data):
            print("bcrypt darbe")
            print(form.profilepic.data)
            #updating firstname
            if form.first_name.data and form.first_name.data != "":
                current_user.first_name = form.first_name.data
            #updating Last Name
            if form.last_name.data and form.last_name.data != "":
                current_user.last_name = form.last_name.data
            #updating phone number
            if form.phonenumber.data and form.phonenumber.data  != "":
                current_user.phonenumber = form.phonenumber.data

            #updating country
            if form.country.data and form.country.data != "":
                current_user.country = form.country.data

            #updating region
            if form.region.data and form.region.data != "":
                current_user.region = form.region.data

            #updating zone
            if form.zone.data and form.zone.data != "":
                current_user.zone = form.zone.data
                
            #updating wereda
            if form.wereda.data and form.wereda.data != "":
                current_user.wereda = form.wereda.data
            #updating wereda
            if form.idnumb.data and form.idnumb.data != "":
                current_user.idnumb = form.idnumb.data
            
            #updating profile pic
            if form.profilepic.data:
                picturefile = save_picture(form.profilepic.data, tobeposted="profilepic")
                current_user.profilepic = picturefile

            
            
            
            storage.new(current_user)
            storage.save()
            return redirect(url_for('myprofile'))
    elif request.method == 'GET':
        form.first_name.data = current_user.first_name
        form.last_name.data = current_user.last_name
        form.phonenumber.data = current_user.phonenumber
        form.country.data = current_user.country

        form.region.data = current_user.region
        form.zone.data = current_user.zone
        form.wereda.data = current_user.wereda
        form.idnumb.data = current_user.idnumb

    return render_template('editprofile.html', title='Edit Profile', form=form)


@app.route("/myprofile/addproperty", methods=['GET', 'POST'])
@login_required
def addproperty():
    form = PropertyForm()
    if form.validate_on_submit():
            subcityname = storage.valCheck("subcity", value=form.subcity.data, cls="SubCity")
            categoryname = storage.valCheck("name", value=form.category.data, cls="Category")
            subcity_id = subcityname.id
            categoryid = categoryname.id
            place = Place(addressLine1=form.addressline1.data, addressLine2=str(form.addressline2.data),
                            userid=current_user.id, subcityid=subcity_id)
            storage.new(place)

            property = Property(name=form.name.data, price=form.price.data,
                                kare=form.kare.data, details=form.details.data,
                                addressLine2=form.addressline2.data,
                                user_id=current_user.id, place_id=place.id,
                                categoryid=categoryid)
            storage.new(property)

            imgfile = save_picture(form.image1.data, tobeposted="property")
            image1 = PropertyImage(name=imgfile, property_id=property.id)
            storage.new(image1)

            if form.image2.data and form.image2.data is not "":
                imgfile = save_picture(form.image2.data, tobeposted="property")
                image2 = PropertyImage(name=imgfile, property_id=property.id)
                storage.new(image2)

                

            if form.image3.data and form.image3.data is not "":
                imgfile = save_picture(form.image3.data, tobeposted="property")
                image3 = PropertyImage(name=imgfile, property_id=property.id)
                storage.new(image3)

            storage.save()
            return redirect(url_for('myprofile'))
    return render_template('postproperty.html', title='My Profile: Post Property', form=form)
            


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', debug=True, port=5000)