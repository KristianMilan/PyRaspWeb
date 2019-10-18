# Author: Junior Tada
import flask
from app import app, log
from flask import render_template, request, redirect, url_for, jsonify
from platform import python_version
import os
import json


@app.route('/')
@app.route('/index')
def index():
	data = None
	try:
		path = f'{os.getcwd()}/app/data/db.json'
		with open(path) as file:
			data = json.load(file)
			if data['schemas']:
				data=data['schemas']
	except Exception as e:
		data = [{'error': e}]
	finally:
		return render_template('index.html', data=data)

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

@app.route('/config', methods=['GET', 'POST'])
def config():
	if request.method == 'POST':	
		try:
			path = f'{os.getcwd()}/app/data/db.json'
			with open(path, 'r+') as file:
				data = json.load(file)
				data['schemas'].append(request.get_json())
				file.seek(0)
				json.dump(data, file, indent=4)
				file.truncate()
			m = 'Save with Success'
			msg = {'value': m, 'status': 'SUCCESS'}
		except Exception as e:
			m = f'Error: {e}'
			msg = {'value': m, 'status': 'ERROR'}
		finally:
			return jsonify(return_msg=msg)
	else:
		return render_template('config.html')

@app.route('/detail/<int:id>')
def detail(id):
    return render_template('detail.html')

@app.route('/_save', methods=['GET', 'POST'])
def _save():
	import pdb
	pdb.set_trace()
	return redirect(url_for('index'))