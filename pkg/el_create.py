#!/usr/bin/python
import sys
import simplejson
from elasticsearch import Elasticsearch
from elasticsearch_dsl import Index

# index music chart - 
#  1) all_music id 1
#	{ "title" : [순위합, 빈도, artist, img_url, youtubr_url, genre(가져온것들만), "popular_genre" : [tf-idf 결과, 가장 인기있는 장르(순위합3정도 리스트로)] }
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
	genie["genie_simil"] = genie_simil
	return genie

def el_create(melon, bugs, genie):
	es_host="127.0.0.1"
	es_port="9200"

#	text, long문제... 해결안됨....
#	for i in all_musics.keys():
#		i = str(i)
	
	es = Elasticsearch([{'host':es_host, 'port':es_port}])

#	json_am = simplejson.dumps(all_musics, ignore_nan = True)
	json_me = simplejson.dumps(melon, ignore_nan = True)
	json_bu = simplejson.dumps(bugs, ignore_nan = True)
	json_ge = simplejson.dumps(genie, ignore_nan = True)

#	index = Index("music_chart", es)

#	index.settings(index = {'mapping': {"properties":{"type": "text"}}, {'ignore_malformed':True}})


# 해당 데이터들이 이미 존재하면 삭제후 다시 생성

	if es.indices.exists(index="melon"):
		es.indices.delete(index="melon")

	if es.indices.exists(index="bugs"):
		es.indices.delete(index="bugs")

	if es.indices.exists(index="genie"):
		es.indices.delete(index="genie")


#	es.create(index='music_chart', doc_type='all_music', id=1, body=json_am)
	es.create(index='melon', doc_type='melon', id=1, body=json_me)
	es.create(index='bugs', doc_type='bugs', id=2, body=json_bu)
	es.create(index='genie', doc_type='genie', id=3, body=json_ge)

"""
	res = es.get(index='music_chart', id=1, ignore=400)

	if not res['found']:
		es.index(index='music_chart', doc_type='all_music', id=1, body=all_musics)
		es.index(index='music_chart', doc_type='melon', id=2, body=melon)
		es.index(index='music_chart', doc_type='bugs', id=3, body=bugs)
		es.index(index='music_chart', doc_type='genie', id=4, body=genie)
	else:
		es.update(index='music_chart', doc_type='all_music', id=1, body=all_musics)
		es.update(index='music_chart', doc_type='melon', id=2, body=melon)
		es.update(index='music_chart', doc_type='bugs', id=3, body=bugs)
		es.update(index='music_chart', doc_type='genie', id=4, body=genie)

	return"""
