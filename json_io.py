#!flask/bin/python

import sys

from flask import Flask, render_template, request, redirect, Response
import random, json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/receiver', methods = ['POST'])
def worker():
	# read json + reply
	data = request.get_json()
	result = 'sampa pagal!!! :['
	
	return result

if __name__ == '__main__':
	# run!
	app.run()