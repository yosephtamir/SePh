#!/usr/bin/python3
""" Starts a Flash Web Application """
from web import app, bcrypt, login_manager
from web.forms import RegistrationForm, CategoryForm, LoginForm, UserProfile
from flask import render_template, redirect, url_for, flash
from models.user import User
from models.category import Category
from models.property import Property
from models import storage
from flask_login import login_user, current_user, logout_user, login_required

# app.jinja_env.trim_blocks = True
# app.jinja_env.lstrip_blocks = True

"""login_manager.login_message_category = 'info'"""

@app.teardown_appcontext
def close_db(error):
    """ Remove the current SQLAlchemy Session """
    storage.close()

@app.route('/', strict_slashes=False)
@app.route('/home', strict_slashes=False)
def home():
    properties = storage.countablefetch(Property).values()
    properties = sorted(properties, key=lambda k: k.name)
    count = 0
    return render_template('seph.html',
                           properties=properties, count = count)

@app.route('/property', strict_slashes=False)
@app.route('/property/<id>', strict_slashes=False)
def property(id=""):
    """ displays a HTML page with a list of cities by states """
    properties = storage.countablefetch(Property).values()
    properties = sorted(properties, key=lambda k: k.name)
    count = 0

    return render_template('seph.html',
                           properties=properties, count = count)
@app.route('/category', strict_slashes=False, methods=["GET", "POST"])
def category():
    form = CategoryForm()
    if form.validate_on_submit():
        category = Category(name=form.name.data)
        storage.new(category)
        storage.save()
    return render_template('category.html', form=form)

@app.route('/register', strict_slashes=False, methods=["GET", "POST"])
def register():
    """ displays a HTML page with a list of cities by states """
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(first_name=form.first_name.data, last_name=form.last_name.data,
            username=form.username.data, email=form.email.data,
            phonenumber=form.phonenumber.data,
            country="form.country.data", region="form.region.data",
            zone="form.zone.data", wereda="form.wereda.data",
            idnumb="form.idnumb.data", profilepic="profiledefault.png",
            password=hashed_password)
        storage.new(user)
        storage.save()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('category'))
    return render_template('register.html', form=form)

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
        current_user
        if bcrypt.check_password_hash(current_user.password, form.password.data):
            #updating firstname
            if form.first_name.data and form.first_name.data is not "":
                current_user.first_name = form.first_name.data
            #updating Last Name
            if form.last_name.data and form.last_name.data is not "":
                current_user.last_name = form.last_name.data
            #updating phone number
            if form.phonenumber.data and form.phonenumber.data  is not "":
                current_user.phonenumber = form.phonenumber.data

            #updating country
            if form.country.data and form.country.data is not "":
                current_user.country = form.country.data

            #updating region
            if form.region.data and form.region.data is not "":
                current_user.region = form.region.data

            #updating zone
            if form.zone.data and form.zone.data is not "":
                current_user.zone = form.zone.data
                
            #updating wereda
            if form.wereda.data and form.wereda.data is not "":
                current_user.wereda = form.wereda.data
            #updating wereda
            if form.idnumb.data and form.idnumb.data is not "":
                current_user.idnumb = form.idnumb.data
            
            #updating wereda
            if form.profilepic.data and form.profilepic.data is not "":
                current_user.profilepic = form.profilepic.data
            
            
            storage.new(current_user)
            storage.save()
            return redirect(url_for('myprofile'))
    return render_template('editprofile.html', title='My Profile', form=form)

if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', debug=True, port=5000)