from flask import Flask
from flask import render_template
from flask import url_for
from flask import request
from flask import redirect

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    return redirect(url_for('add'))

@app.route('/add',methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        a = request.form['adder1']
        b = request.form['adder2']
        a = int(a)
        b = int(b)
        c = a+b
        return render_template('index.html', message = str(c))
    return render_template('index.html')


if __name__ == '__main__':
    app.run(port=1111)
