# Author: Junior Tada
from app import app, log
from flask import render_template
import flask
from platform import python_version


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    info = {}
    info['Author'] = 'Junior Tada'
    info['Email'] = 'juniortada@gmail.com'
    info['pyraspweb'] = '0.1'
    info['python'] = python_version()
    info['flask'] = flask.__version__
    return render_template('about.html', info=info)

@app.route('/backup')
def backup():
    return render_template('backup.html')

@app.route('/detail/<int:id>')
def detail(id):
    return render_template('detail.html')