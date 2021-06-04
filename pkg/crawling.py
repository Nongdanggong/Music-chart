#!/usr/bin/python3
#-*- coding: utf-8 -*-

import re
import requests
import numpy
from bs4 import BeautifulSoup
from flask import Flask, render_template
from nltk import word_tokenize

def melon():
#if __name__ == '__main__':

#기본 데이터가 될 dictionary {곡 이름 : [순위합 / 아티스트 / 앨범 사진 url / youtube url /  장르(뽑아온 것만), (+탑5 youtube_id)]} 형태임.
	melon={}
	
#우리 사이트와 유사도를 비교하기 위한 각 사이트의 곡 리스트들을 나타낸것
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
		img = html_image[i].get('src')
		url_youtube = 'https://www.youtube.com/results?search_query='+title

		melon[title] = [i+1, 1, artist, img, url_youtube]

#	print(melon)

	return melon, melon_list


def bugs(all_music):
#if __name__ == '__main__':

#앞선 곡의 정보들은 파라미터로 받음 (이건 테스트용 test_crawling 실행할때 주석 제거해주세요)

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
# url에 날짜가 반영되므로 첫 지니 crawling시 다음 페이지 url을 html태그에서 따로 받아옴

	html_add_url = html.find("div", attrs={'class':'page-nav rank-page-nav'})

	add_url = html_add_url.find_all('a')[1].get("href")

	next_url = u'https://www.genie.co.kr/chart/top200'+add_url
			
	header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'}
	req = requests.get(next_url, headers = header) 

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

def genre(all_list,num):
	
	repeat = 0
	
	for key in all_list.keys():
		
		repeat += 1

		url = u'https://www.melon.com/search/total/index.htm?q=%s&section=&linkOrText=T&ipath=srch_form' % key
		header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'}
		req = requests.get(url, headers = header) 
		html = BeautifulSoup(req.content, "html.parser")

#		genre 함수 실행시 html_idnum 에서 오류 발생 -> 밑의 코드 주석 해제후 실행 해보기 -> "페이지를 찾을 수 없습니다" 뜰 시 멜론에서 ip가 차단당한것, 다른 ip로 접속하여 (휴대폰 핫스팟 등) 실행 시 실행 가능 할 것 (이 때는 다시 주석 처리 해주기)
#		print(html.text)


		html_chart = html.find('tbody')

		html_idnum = html_chart.find("div", attrs={'class':'wrap pd_none'})
		idnum_string = html_idnum.find("button").get("onclick")

		numbers = re.findall("\d+", idnum_string)

		# 제목에 숫자가 있는 경우 idnum을 잘못 인식하여 에러가 나는 것을 방지
		for i in numbers:
			inti = int(i)
			if (inti > 100000):
				idnum = i 
				break

		url_genre = 'https://www.melon.com/song/detail.htm?songId='+idnum
		req_genre = requests.get(url_genre, headers = header) 

		html = BeautifulSoup(req_genre.content, "html.parser")
		html_info = html.find("div", attrs={'class':'section_info'})
		if(html_info == None):
			all_list[key].append('기타')
			continue
		html_dl = html_info.find("dl")
		genre1 = html_dl.text.replace("\n"," ")
		genre2 = word_tokenize(genre1)
		for i in range(len(genre2)):
			if(genre2[i]=='장르'):
				genre = genre2[i+1]
				if (genre == 'R'):
					genre = 'R&B'
				break

		all_list[key].append(genre)

		if (repeat >= num):
			break

	return all_list 
