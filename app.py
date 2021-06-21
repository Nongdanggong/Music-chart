#!/usr/bin/python3
# -*- coding: utf-8 -*-

import argparse
import subprocess
from flask import Flask, jsonify
from flask import render_template
from flask import request
from pkg.crawling import *


app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')





if __name__ == '__main__':
	try:
		parser = argparse.ArgumentParser(description="")
		parser.add_argument('--listen-port', type=str, required=True, help='REST service listen port')
		args = parser.parse_args()
		listen_port = args.listen_port
	except Exception as e:
		print('Error: %s' % str(e))

ipaddr="127.0.0.1"
print ("Starting the service with ip_addr="+ipaddr)

app.run(debug=False, host=ipaddr, port=int(listen_port))
