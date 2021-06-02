#!/usr/bin/python
import sys
from elasticsearch import Elasticsearch

# index music chart - 
#  1) all_music id 1
#	{ "title" : [순위합, 빈도, artist, img_url, youtubr_url, "popular_genre" : [tf-idf 결과, 가장 인기있는 장르(순위합3정도 리스트로)] }
#  2) melon id 2
#	{"list" : "100개의 순위 리스트", "genre" : "각 순위 노래들의 장르", "similarity" : "종합 차트와의 유사도(cosine)"}
		
def struct_all_music(all_music, list):
	all_music["tf-idf"] = list 
	return all_music

def struct_melon(melon_list, melon_simil):
	melon = {}
	melon["list"] = melon_list
	melon["melon_simil"] = melon_simil
	return melon

def struct_bugs(bugs_list, bugs_simil):
	bugs = {}
	bugs["list"] = bugs_list
	bugs["bugs_simil"] = bugs_simil
	return bugs

def struct_genie(genie_list, genie_simil):
	genie = {}
	genie["list"] = genie_list
	genie["melon_simil"] = genie_simil
	return genie

def el_create(all_music, melon, bugs, genie):
	es_host="127.0.0.1"
	es_port="9200"

	es = Elasticsearch([{'host':es_host, 'port':es_port}])


	res = es.get(index='music_chart', doc_type='all_music', id=1, body=all_music)

	if not res['found']:
		es.index(index='music_chart', doc_type='all_music', id=1, body=all_music)
		es.index(index='music_chart', doc_type='melon', id=2, body=melon)
		es.index(index='music_chart', doc_type='bugs', id=3, body=bugs)
		es.index(index='music_chart', doc_type='genie', id=4, body=genie)
	else:
		es.update(index='music_chart', doc_type='all_music', id=1, body=all_music)
		es.update(index='music_chart', doc_type='melon', id=2, body=melon)
		es.update(index='music_chart', doc_type='bugs', id=3, body=bugs)
		es.update(index='music_chart', doc_type='genie', id=4, body=genie)


	return
