#!/usr/bin/python3
# -*- coding: utf-8 -*-

import re
import requests
import json
import argparse
import subprocess

from bs4 import BeautifulSoup
from flask import Flask, jsonify
from flask import render_template
from flask import request
from pkg.crawling import *
from pkg.list_sort import *
from pkg.similar import *
from pkg.tf_idf import *
from pkg.el_create import *
from pkg.create_jsons import *

app = Flask(__name__)

@app.route('/')
def input():
	return render_template('home.html')

@app.route('/chart')
def index():
	value=int(request.args.get('input'))
	all_music = {}

	all_music, melon_list = melon()
	all_music, bugs_list = bugs(all_music)
	all_music, genie_list = genie(all_music)
	#위 10개까지만 장르가 등록됩니다. (test용)
	all_musics = list_sort(all_music)
	all_musics = genre(all_musics,value)

	# 순위(number=100) 100까지 유사도 분석
	melon_simil=cos_similarity(all_musics,melon_list,value)
	bugs_simil=cos_similarity(all_musics,bugs_list,value)
	genie_simil=cos_similarity(all_musics,genie_list,value)

	similars = [{"melon":melon_simil}, {"bugs":bugs_simil}, {"genie":genie_simil}]
	with open('./static/similars.json', 'w', encoding='utf-8') as f:
	    f.write("similars = '")
	with open('./static/similars.json', 'a', encoding='utf-8') as f:
	    json.dump(similars, f) # /statics에 similars.json  파일생성
	with open('./static/similars.json', 'a', encoding='utf-8') as f:
	    f.write("';")

	# TF_IDF(all_musics)
	all_tf = tf_idf(all_musics, value)
	#print('\n\n', all_tf) 

	#전체 자료 dictionary화 (elasticsearch를 위한 자료 구조화)
	all_musics_d = struct_all_music(all_musics, all_tf)
	melon_d = struct_melon(melon_list, melon_simil)
	bugs_d = struct_bugs(bugs_list, bugs_simil)
	genie_d = struct_genie(genie_list, genie_simil)

	# elasticsearch 자료 생성
	el_create(all_musics_d, melon_d, bugs_d, genie_d)
	#el_create(melon, bugs, genie)

	create_jsons() # /statics에 ranks.json, genres.json 파일생성
	return render_template('index.html', rank_length = value, ID = 'PLPjXscyDGRTC_E0oL1EJX92gIsXMkm0Wy')

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
