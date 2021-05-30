#!/usr/bin/python3
#-*- coding: utf-8 -*-

import re
import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template

def melon():
#if __name__ == '__main__':

#기본 데이터가 될 dictionary {곡 이름 : [순위합 / 아티스트 / 앨범 사진 url / 유튜브 url / 장르(tf-idf하기 위한 string)]} 형태임.
	melon={}
	
#우리 사이트와 유사도를 비교하기 위한 각 사이트의 곡 리스트들을 string으로 나타낸것
	melon_list=' '

	url = u'https://www.melon.com/chart/index.htm'
	header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'}
	req = requests.get('https://www.melon.com/chart/index.htm', headers = header) 

	html = BeautifulSoup(req.content, "html.parser")

	html_chart = html.find('tbody')

	html_title = html_chart.find_all("div", attrs={'class':'ellipsis rank01'})
	html_artist = html_chart.find_all("div", attrs={'class':'ellipsis rank02'})
	html_image = html_chart.find_all("img")
	html_genre = html_chart.find_all("tr")

	for i in range(100):
		title = html_title[i].text.strip()
		melon_list = melon_list + title + ' '
		artist = html_artist[i].find('a').text.strip()
		url_youtube = 'https://www.youtube.com/results?search_query='+title
		img = html_image[i].get('src')

#장르는 멜론 함수에서 크롤링 후 종합차트 완성 뒤 그 중 없는 것만 따로 크롤링
#이 과정에서 시간이 굉장히 많이 걸리므로 테스트할 떄는 주석처리 하고 할것
#이 과정을 시행하다가 중간에 멈추면 오류메세지가 뜸. 끝까지 수행할 때는 뜨지 않으니 안심할것
		song_num = html_genre[i].get('data-song-no')
		url_genre = 'https://www.melon.com/song/detail.htm?songId='+song_num
		req_genre = requests.get(url_genre, headers = header) 
		html = BeautifulSoup(req_genre.content, "html.parser")
		html_info = html.find("div", attrs={'class':'section_info'})
		html_dl = html_info.find("dl")
		genre = html_dl.text.replace("\n"," ")

		melon[title] = [i+1, artist, img, url_youtube, genre]

	return melon, melon_list
