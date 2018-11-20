# Author: Junior Tada
from flask import Flask, render_template
import logging
from logging.handlers import RotatingFileHandler
import locale
import re

# Define app Flask
app = Flask(__name__)
__version__ = '0.1'
__author__ = 'Junior Tada'

# config
app.config.from_json("config.json")

# log
formatter = logging.Formatter('%(levelname)s: %(asctime)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')
handler = RotatingFileHandler('app.log', maxBytes=100000, backupCount=1)
handler.setFormatter(formatter)
handler.setLevel(logging.INFO)
app.logger.addHandler(handler)
log = app.logger

# HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# HTTP error handling
@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

# main application
from app.controller import main