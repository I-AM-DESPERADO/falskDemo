# -*- coding: utf-8 -*-
__author__ = 'tz'
__date__ = '2017-10-04 13:08'


from flask import Flask

from flask_mongoengine import MongoEngine

app = Flask(__name__)
app.config.from_object('config')
db = MongoEngine(app)


from app import views,models

