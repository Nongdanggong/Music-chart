#!/usr/bin/python3
#-*- coding: utf-8 -*-

import re
import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template
from pkg.crawling import *
from pkg.list_sort import *
from pkg.similar import *
#from pkg.tf_idf import *
from pkg.el_create import *


all_music = {}

all_music, melon_list = melon()
all_music, bugs_list = bugs(all_music)
all_music, genie_list = genie(all_music)
#위 10개까지만 장르가 등록됩니다. (test용)
all_musics = list_sort(all_music)
all_musics = genre(all_musics,100)

#for i in all_musics.values():
#	print(i)
#print(all_musics,'\n\n')
#print(melon_list,'\n\n')
#print(bugs_list, '\n\n')
#print(genie_list,'\n\n')

# 순위(number=100) 100까지 유사도 분석
melon_simil=cos_similarity(all_musics,melon_list,50)
bugs_simil=cos_similarity(all_musics,bugs_list,50)
genie_simil=cos_similarity(all_musics,genie_list,50)
	
print("melon similarity = > ",melon_simil)
print("bugs  similarity = > ",bugs_simil)
print("genie similarity = > ",genie_simil)

# TF_IDF(all_musics)
all_tf = tf_idf(all_musics, 100)
print(all_tf) 

#전체 자료 dictionary화 (elasticsearch를 위한 자료 구조화)
all_music = struct_all_music(all_music, #tf_idf)
melon = struct_melon(melon_list, melon_genre, melon_simil)
bugs = struct_bugs(bugs_list, bugs_genre, bugs_simil)
genie = struct_genie(genie_list, genie_genre, bugs_simli)

print(all_music)
print(melon)
print(bugs)
print(genie)

# elasticsearch 자료 생성
el_create(all_music, melon, bugs, genie)
