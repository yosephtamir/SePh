#!/usr/bin/python3
""" Starts a Flash Web Application """
from flask_bcrypt import Bcrypt
from models import storage
from models.user import User

user = User(first_name=form.first_name.data, last_name=form.last_name.data,
            username=form.username.data, email=form.email.data,
            phonenumber=form.phonenumber.data,
            country="form.country.data", region="form.region.data",
            zone="form.zone.data", wereda="form.wereda.data",
            idnumb="form.idnumb.data", profilepic=f"orm.profilepic.data",
            password=hashed_password)
storage.new(user)
storage.save()