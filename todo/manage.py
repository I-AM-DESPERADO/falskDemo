# -*- coding: utf-8 -*-
__author__ = 'tz'
__date__ = '2017-10-04 13:07'

from app import app
from app.models import Todo
from flask_script import Manager


manager = Manager(app)

@manager.command
def save():
    todo = Todo(content = 'study flask')
    todo.save()

if __name__ == '__main__':
    manager.run()