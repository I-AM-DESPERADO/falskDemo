# !/usr/bin/python
from __future__ import unicode_literals
# -*- coding: utf-8 -*-

__author__ = 'AidChow'

import os
# from flask.ext.script import Manager, Shell
from flask_script import Manager,Shell
from app import create_app

app = create_app(os.getenv('NEWS_CONFIG') or 'default')


manager = Manager(app)


def make_shell_context():
    return dict(app=app)


manager.add_command("shell", Shell(make_context=make_shell_context()))

if __name__ == '__main__':
    manager.run()
