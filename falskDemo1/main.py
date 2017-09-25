# -*- coding: utf-8 -*-
from flask import Flask
from flask import request
from flask import render_template
from flask import redirect

from wtforms import Form,TextField,PasswordField,validators
__author__ = 'tz'
__date__ = '2017-09-25 15:59'

app = Flask(__name__)


class LoginForm(Form):
    username = TextField('username', [validators.Required()])
    password = PasswordField('password', [validators.Required()])


@app.route('/user', methods=["GET", "POST"])
def login():
    myForm = LoginForm(request.form)
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'tz' and password == '123':
            return redirect('http://www.baidu.com')
        else:
            message = 'Login Failed'
            return render_template('index1.html', message=message)
    return render_template('index1.html', form=myForm)

if __name__ == '__main__':
    app.run(port=1111)
