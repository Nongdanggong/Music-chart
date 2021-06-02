#!/usr/bin/python3
#-*- coding: utf-8 -*-

import re
import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template
from pkg.crawling import *
from pkg.list_sort import *
from pkg.similar import *
from pkg.tf_idf import *

all_music = {}

all_music, melon_list = melon()
all_music, bugs_list = bugs(all_music)
all_music, genie_list = genie(all_music)
#위 10개까지만 장르가 등록됩니다. (test용)
all_musics = list_sort(all_music)

#melon_genre = genre(melon_list,100)
#print(melon_genre)
#bugs_genre = genre(bugs_list,100)
#print(bugs_genre)
genie_genre = genre(genie_list,100)
print(genie_genre)

#for i in all_musics.values():
#	print(i)
#print(all_musics,'\n\n')
#print(melon_list,'\n\n')
#print(bugs_list, '\n\n')
#print(genie_list,'\n\n')

# 순위(number=100) 100까지 유사도 분석
melon_simil=cos_similarity(all_musics,melon_list,100)
bugs_simil=cos_similarity(all_musics,bugs_list,100)
genie_simil=cos_similarity(all_musics,genie_list,100)
	
print("melon similarity = > ",melon_simil)
print("bugs  similarity = > ",bugs_simil)
print("genie similarity = > ",genie_simil)

#TF_IDF(all_musics)
