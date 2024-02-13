#!/usr/bin/python3
""" Starts a Flash Web Application """
from web import app, bcrypt, login_manager
from web.forms import RegistrationForm, CategoryForm
from flask import render_template, redirect, url_for, flash
from models.user import User
from models.category import Category
from models.property import Property
from models import storage

# app.jinja_env.trim_blocks = True
# app.jinja_env.lstrip_blocks = True

"""login_manager.login_view = 'login'
login_manager.login_message_category = 'info'"""

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
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(first_name=form.first_name.data, last_name=form.last_name.data,
            username=form.username.data, email=form.email.data,
            phonenumber=form.phonenumber.data,
            country="form.country.data", region="form.region.data",
            zone="form.zone.data", wereda="form.wereda.data",
            idnumb="form.idnumb.data", profilepic=f"orm.profilepic.data",
            password=hashed_password)
        print(user)
        storage.new(user)
        storage.save()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('category'))
    flash('not created', 'success')
    return render_template('register.html', form=form)

if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', debug=True, port=5000)