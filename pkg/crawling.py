#usr/bin/python3
#-*- coding: utf-8 -*-

import re
import requests
import numpy
from bs4 import BeautifulSoup
from flask import Flask, render_template
from nltk import word_tokenize

def melon():
#if __name__ == '__main__':

#기본 데이터가 될 dictionary {곡 이름 : [순위합 / 아티스트 / 앨범 사진 url / 유튜브 url / 장르(tf-idf하기 위한 string)]} 형태임.
	melon={}
	
#우리 사이트와 유사도를 비교하기 위한 각 사이트의 곡 리스트들을 string으로 나타낸것
	melon_list=[]

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
		melon_list.append(title)
		artist = html_artist[i].find('a').text.strip()
		url_youtube = 'https://www.youtube.com/results?search_query='+title
		img = html_image[i].get('src')
		
		melon[title] = [i+1, 1, artist, img, url_youtube]

	return melon, melon_list


def bugs(all_music):
#if __name__ == '__main__':

#앞선 곡의 정보들은 파라미터로 받음 (이건 테스트용 test_crawling 실행할때 주석 제거해주세요)
#	all_music = {}
#우리 사이트와 유사도를 비교하기 위한 각 사이트의 곡 리스트들을 string으로 나타낸것

	bugs_list=[]

	url = u'https://music.bugs.co.kr/chart'
	header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'}
	req = requests.get(url, headers = header) 

	html = BeautifulSoup(req.content, "html.parser")

	html_chart = html.find('tbody')

	html_title = html_chart.find_all("p", attrs={'class':'title'})
	html_artist = html_chart.find_all("p", attrs={'class':'artist'})
	html_image = html_chart.find_all("img")

	for i in range(100):
		title = html_title[i].text.strip()
		bugs_list.append(title)
		artist = html_artist[i].find('a').text.strip()
		url_youtube = 'https://www.youtube.com/results?search_query='+title
		img = html_image[i].get('src')

		if (title in all_music):
			all_music[title][0] += i+1
			all_music[title][1] += 1
		else:
			all_music[title] = [i+1, 1, artist, img, url_youtube]

	return all_music, bugs_list



def genie(all_music):
#if __name__ == '__main__':

#	all_music = {}
	
	genie_list=[]

	url = u'https://www.genie.co.kr/chart/top200'
	header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'}
	req = requests.get(url, headers = header) 

	html = BeautifulSoup(req.content, "html.parser")

	html_chart = html.find('tbody')

	html_title = html_chart.find_all("a", attrs={'class':'title ellipsis'})
	html_artist = html_chart.find_all("a", attrs={'class':'artist ellipsis'})
	html_image = html_chart.find_all("img")

	for i in range(50):
		title = html_title[i].text.strip()
		genie_list.append(title)
		artist = html_artist[i].text.strip()
		url_youtube = 'https://www.youtube.com/results?search_query='+title
		img = html_image[i].get('src')

		if (title in all_music):
			all_music[title][0] += i+1
			all_music[title][1] += 1 
		else:
			all_music[title] = [i+1, 1, artist, img, url_youtube]

#2번째 페이지 (51~100)	
	url = u'https://www.genie.co.kr/chart/top200?ditc=D&ymd=20210531&hh=01&rtm=Y&pg=2'
	header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'}
	req = requests.get(url, headers = header) 

	html = BeautifulSoup(req.content, "html.parser")

	html_chart = html.find('tbody')

	html_title = html_chart.find_all("a", attrs={'class':'title ellipsis'})
	html_artist = html_chart.find_all("a", attrs={'class':'artist ellipsis'})
	html_image = html_chart.find_all("img")

	for i in range(50):
		title = html_title[i].text.strip()
		genie_list.append(title)
		artist = html_artist[i].text.strip()
		url_youtube = 'https://www.youtube.com/results?search_query='+title
		img = html_image[i].get('src')

		if (title in all_music):
			all_music[title][0] += i+51
			all_music[title][1] += 1
		else:
			all_music[title] = [i+51, 1, artist, img, url_youtube]

#	print(all_music)

	return all_music, genie_list


#시간이 오래걸리므로 테스트할때는 실행하지 않는 것 추천
#이 과정을 시행하다가 중간에 멈추면 오류메세지가 뜸. 끝까지 수행할 때는 뜨지 않으니 안심할것

def genre(all_music, num):
	
	repeat = 0
	list =[]
	for key in all_music.keys():
		
		repeat += 1

		#url = u'https://www.melon.com/search/song/index.htm?q=%s&section=&searchGnbYn=Y&kkoSpl=N&kkoDpType=&ipath=srch_form' % key 
		url = u'https://www.genie.co.kr/search/searchSong?query=%s&Coll=' % key

		header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'}
		req = requests.get(url, headers = header) 
		html = BeautifulSoup(req.content, "html.parser")
		html_chart = html.find('tbody')
		#if(html_chart == None):
		#	continue

		html_idnum = html_chart.find("td", attrs={'class':'link'})
		idnum_string = html_idnum.find("a").get("onclick")

		numbers = re.findall("\d+", idnum_string)

		url_genre = 'https://www.genie.co.kr/detail/songInfo?xgnm=92749703='+numbers[0]
		req_genre = requests.get(url_genre, headers = header) 

		html = BeautifulSoup(req_genre.content, "html.parser")
		html_info = html.find("div", attrs={'class':'info-zone'})
		if(html_info == None):
			all_music[key].append('0')
			continue
		html_attr = html_info.find("span", attrs={'class':'attr'})
		genre1 = html_attr.text.replace("\n"," ")
		genre2 = word_tokenize(genre1)
		for i in range(len(genre2)):
			if(genre2[i]=='장르'):
				genre = genre2[i+1]
				break

		all_music[key].append(genre)

		if (repeat >= num):
			break

	return all_music

