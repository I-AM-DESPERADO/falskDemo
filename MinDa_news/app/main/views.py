# !/usr/bin/python
# -*- coding: utf-8 -*-

from . import main

__author__ = 'AidChow'


@main.route('/', methods=['GET'])
def index():
    return 'Congretulations Runserver Success!!!'
