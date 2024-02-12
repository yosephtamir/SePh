#!/usr/bin/python3
from flask_bcrypt import Bcrypt
from flask import Flask
from flask_login import LoginManager, login_user, current_user, logout_user, login_required

app = Flask(__name__)
# app.jinja_env.trim_blocks = True
# app.jinja_env.lstrip_blocks = True
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

bcrypt = Bcrypt(app)
login_manager = LoginManager(app)