# !/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Blueprint

__author__ = 'AidChow'

main = Blueprint('main', __name__)

from . import views
