#!flask/bin/python


from __future__ import with_statement
from contextlib import closing

# all the imports
import sqlite3
import json
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash

from models import *

 
# configuration
DATABASE = '/tmp/flaskr.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'




# create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)



app.config.from_envvar('FLASKR_SETTINGS', silent=True)

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])


def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql') as f:
            db.cursor().executescript(f.read())
        db.commit()

@app.before_request
def before_request():
    g.db = connect_db()
 
@app.teardown_request
def teardown_request(exception):
    g.db.close()

@app.route('/')
def show_entries():
    cur = g.db.execute('select title, text from entries order by id desc')
    entries = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
    return render_template('index.html', entries=entries)

@app.route('/contacts')
@db_session
def index():
    return render_template("contacts.html")

@app.route('/catalog')
@db_session
def get_categories():
    categories = Category.name
    return to_json(db, {'categories': name})





if __name__ == '__main__':
	app.run(host='0.0.0.0',debug = True)

