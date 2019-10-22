# Author: Junior Tada
import flask
from app import app, log
from flask import render_template, request, redirect, url_for, jsonify, send_from_directory
from platform import python_version
import os
import json

path = f'{os.getcwd()}/app/data/db.json'

@app.route('/')
@app.route('/index')
def index():
	objs = None
	try:
		path = f'{os.getcwd()}/app/data/db.json'
		with open(path) as file:
			data = json.load(file)
			if data['schemas'] and (len(data['schemas']) > 0):
				objs=data['schemas']
	except Exception as e:
		objs = [{'error': e}]
	finally:
		return render_template('index.html', data=objs)

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
			with open(path, 'r+') as file:
				data = json.load(file)
				data['schemas'].append(request.get_json())
				file.seek(0)
				json.dump(data, file, indent=4)
				file.truncate()
			m = 'Save Success'
			msg = {'value': m, 'status': 'SUCCESS'}
		except Exception as e:
			m = f'Save {e}'
			msg = {'value': m, 'status': 'ERROR'}
		finally:
			return jsonify(return_msg=msg)
	else:
		return render_template('config.html')

@app.route('/detail/<int:id>')
def detail(id):
    data = None
    try:
        path = f'{os.getcwd()}/app/data/db.json'
        with open(path) as file:
            data = json.load(file)
            data = data['schemas'][int(id)]
            data['id'] = id
    except Exception as e:
        data = [{'error': e}]
    finally:
        return render_template('detail.html', data=data)

@app.route('/download/<path:file>', methods=['GET', 'POST'])
def download(file):
	path = f'{os.getcwd()}/app/data/'
	return send_from_directory(directory=path, filename=file)

@app.route('/_delete', methods=['POST'])
def _delete():
    data = None
    try:
        id = int(request.get_data().decode('utf-8').replace('id=',''))
        if id >= 0:
            m = 'Delete Sucess'
            msg = {'value': m, 'status': 'SUCCESS'}
            with open(path, 'r+') as file:
                data = json.load(file)
                data['schemas'].pop(id)
                file.seek(0)
                json.dump(data, file, indent=4)
                file.truncate()
        else:
            m = 'Error: Invalid ID!'
            msg = {'value': m, 'status': 'ERROR'}
    except Exception as e:
        m = f'Delete {e}'
        msg = {'value': m, 'status': 'ERROR'}
    finally:
        return jsonify(return_msg=msg)

@app.route('/_toggle_status', methods=['POST'])
def _toggle_status():
	print('toggle')
	try:
		id = 1
		if id >= 0:
			with open(path, 'r+') as file:
				data = json.load(file)
				if data['schemas'][id]
					print(data['schemas'][id])
					msg = {'value': 'success', 'status': 'SUCCESS'}
	except Exception as e:
		msg = {'value': e, 'status': 'ERROR'}
	finally:
		return jsonify(return_msg=msg)