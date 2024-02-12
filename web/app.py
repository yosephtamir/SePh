#!/usr/bin/python3
""" Starts a Flash Web Application """
from flask_bcrypt import Bcrypt
from models import storage
from models.user import User
from models.category import Category
from models.property import Property
from os import environ
from flask import Flask, render_template, redirect, url_for, flash
from forms import RegistrationForm, LoginForm
from flask_login import LoginManager, login_user, current_user, logout_user, login_required
app = Flask(__name__)
# app.jinja_env.trim_blocks = True
# app.jinja_env.lstrip_blocks = True


bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'


@app.teardown_appcontext
def close_db(error):
    """ Remove the current SQLAlchemy Session """
    storage.close()



@app.route('/property', strict_slashes=False)
@app.route('/property/<id>', strict_slashes=False)
def property(id=""):
    """ displays a HTML page with a list of cities by states """
    properties = storage.countablefetch(Property).values()
    properties = sorted(properties, key=lambda k: k.name)
    count = 0

    return render_template('seph.html',
                           properties=properties, count = count)

@app.route('/register', strict_slashes=False)
def register():
    """ displays a HTML page with a list of cities by states """
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(first_name=form.first_name.data, last_name=form.last_name.data,
                    username=form.username.data, email=form.email.data, phonenumber=form.phonenumber.data,
                    country=form.country.data, region=form.region.data,
                    zone=form.zone.data, wereda=form.wereda.data,
                    idnumb=form.idnumb.data, profilepic=form.profilepic.data,
                    password=hashed_password)
        storage.new(user)
        storage.save()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', debug=True, port=5000)