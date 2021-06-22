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

"""
all_music = {}

all_music, melon_list = melon()
all_music, bugs_list = bugs(all_music)
all_music, genie_list = genie(all_music)
#위 10개까지만 장르가 등록됩니다. (test용)
all_musics = list_sort(all_music)
all_musics = genre(all_musics,10)

# 순위(number=100) 100까지 유사도 분석
melon_simil=cos_similarity(all_musics,melon_list,10)
bugs_simil=cos_similarity(all_musics,bugs_list,10)
genie_simil=cos_similarity(all_musics,genie_list,10)

similars = [{"melon":melon_simil}, {"bugs":bugs_simil}, {"genie":genie_simil}]
with open('./static/similars.json', 'w', encoding='utf-8') as f:
    f.write("similars = '")
with open('./static/similars.json', 'a', encoding='utf-8') as f:
    json.dump(similars, f) # /statics에 similars.json  파일생성
with open('./static/similars.json', 'a', encoding='utf-8') as f:
    f.write("';")

# TF_IDF(all_musics)
all_tf = tf_idf(all_musics, 10)
#print('\n\n', all_tf) 

#전체 자료 dictionary화 (elasticsearch를 위한 자료 구조화)
all_musics = struct_all_music(all_musics, all_tf)
melon = struct_melon(melon_list, melon_simil)
bugs = struct_bugs(bugs_list, bugs_simil)
genie = struct_genie(genie_list, genie_simil)

# elasticsearch 자료 생성
el_create(all_musics, melon, bugs, genie)
#el_create(melon, bugs, genie)

create_jsons() # /statics에 ranks.json, genres.json 파일생성
"""

app = Flask(__name__)

@app.route('/')
def input():
	return render_template('home.html')

@app.route('/chart')
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
