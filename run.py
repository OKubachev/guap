#!flask/bin/python


from __future__ import with_statement
from contextlib import closing

# all the imports
import sqlite3
import json
from js import *
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash

from models import *

 
# configuration
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'


# create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)



app.config.from_envvar('FLASKR_SETTINGS', silent=True)

@app.before_request
def before_request():
    pass
 
@app.teardown_request
def teardown_request(exception):
    pass

@app.route('/')
@db_session
def show_entries():
    return render_template('index.html')

@app.route('/contacts')
@db_session
def index():
    return render_template("contacts.html")

@app.route('/catalog')
@db_session
def get_categories():
    categories = Category.select().order_by(Category.name)
    return render_template('catalog.html', categories=categories)

@app.route('/catalog/<name>')
@db_session
def clothing(name):
    cat = Category.get(name=name)
    return render_template('clothing.html', cat=cat)


if __name__ == '__main__':



	app.run(host='0.0.0.0',debug = True)

