#!/usr/bin/python
import sys
import simplejson
from elasticsearch import Elasticsearch
from elasticsearch_dsl import Index

# index music chart - 
#  1) all_music id 1
#	{ "title" : [순위합, 빈도, artist, img_url, youtubr_url, genre(가져온것들만), "popular_genre" : [tf-idf 결과 인기있는 장르 순위 리스트로] }
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

#def el_create(melon, bugs, genie):
def el_create(all_musics, melon, bugs, genie):
	es_host="127.0.0.1"
	es_port="9200"

#	text, long문제... 해결안됨....
#	for i in all_musics.keys():
#		str(i)
	
	es = Elasticsearch([{'host':es_host, 'port':es_port}])
	
	dictnum = len(all_musics)
	rep = 0

	for i in all_musics.values():
		i[0] = str(i[0])
		i[1] = str(i[1])
		rep += 1
		if (rep == dictnum -1):
			break


	tf_num = len(all_musics["tf-idf"])
	repeat = 0

	print(all_musics["tf-idf"])

	for i in all_musics["tf-idf"]:
		bestr = "%s --> %s" % (i[0], i[1])
		all_musics["tf-idf"][repeat] = bestr
		
		repeat += 1
		if (repeat == tf_num):
			break;


#		print(type(i))

	print(all_musics["tf-idf"])

	json_am = simplejson.dumps(all_musics, ignore_nan = True)
	json_me = simplejson.dumps(melon, ignore_nan = True)
	json_bu = simplejson.dumps(bugs, ignore_nan = True)
	json_ge = simplejson.dumps(genie, ignore_nan = True)

#	index = Index("music_chart", es)

#	index.settings(index = {'mapping': {"properties":{"type": "text"}}, {'ignore_malformed':True}})


# 해당 데이터들이 이미 존재하면 삭제후 다시 생성

	if es.indices.exists(index="all_musics"):
		es.indices.delete(index="all_musics")

	if es.indices.exists(index="melon"):
		es.indices.delete(index="melon")

	if es.indices.exists(index="bugs"):
		es.indices.delete(index="bugs")

	if es.indices.exists(index="genie"):
		es.indices.delete(index="genie")


	es.create(index='all_musics', doc_type='all_musics', id=1, body=json_am)
	es.create(index='melon', doc_type='melon', id=2, body=json_me)
	es.create(index='bugs', doc_type='bugs', id=3, body=json_bu)
	es.create(index='genie', doc_type='genie', id=4, body=json_ge)

	return

