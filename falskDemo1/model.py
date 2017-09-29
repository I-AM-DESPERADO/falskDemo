# -*- coding: utf-8 -*-
__author__ = 'tz'
__date__ = '2017-09-29 20:22'

from flask import Flask

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123@localhost/flaskdemo'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(32),unique=True)
    password = db.Column(db.String(32))

    def __init__(self, username, password):
        self.name = username
        self.password = password

db.create_all()