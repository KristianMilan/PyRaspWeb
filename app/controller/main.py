# Author: Junior Tada
import flask
from app import app, log
from flask import render_template
from platform import python_version
import os
import json


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

@app.route('/config')
def config():
	path = f'{os.getcwd()}/app/data/db.json'
	with open(path) as file:
		data = json.load(file)
		print(data['schemas'])
		return render_template('config.html', data=data['schemas'])

@app.route('/detail/<int:id>')
def detail(id):
    return render_template('detail.html')