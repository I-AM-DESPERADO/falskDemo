# ！/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Blueprint

__author__ = 'AidChow'

news = Blueprint('news', __name__)

from . import view, error
