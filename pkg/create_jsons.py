#!/bin/python3
#-*- coding: utf-8 -*-

import json
import re
import requests

def save_image(img_url, rank, title, artist):
    response = requests.get(img_url)
    content = response.content
    filename = "./templates/images/{}.jpeg".format(rank)
    file = open(filename, "wb")
    file.write(content)

#if __name__ == '__main__':
def create_jsons():
    with open('file_am.json','r') as f:
        json_data = json.load(f)

    ranks = []
    genres = []
    cnt = 0
    k = 0
    for i in json_data['_source'].keys():
        if i == "tf-idf":
            for k in range(len(json_data['_source'][i])):
                genre = {"genre" : json_data['_source'][i][k].split(' --> ')[0], "ratio" : json_data['_source'][i][k].split(' --> ')[1]}
                genres.append(genre)
            break
        rank = {"title" : re.sub("\'","\u2032", i), "singer" : json_data['_source'][i][2], "img" : json_data['_source'][i][3]}
        url = json_data['_source'][i][3]
        if 'genie' in url:
            url = "http:"+url
#        save_image(url, json_data['_source'][i][1], i, json_data['_source'][i][2])
        ranks.append(rank)


#    print(ranks)
#    print(genres)

    with open('./static/ranks.json', 'w', encoding = 'utf-8') as f:
        data = "ranks = '"
        f.write(data)
    with open('./static/ranks.json', 'a', encoding='utf-8') as f:
        json.dump(ranks, f)
    with open('./static/ranks.json', 'a', encoding='utf-8') as f:
        data = "';"
        f.write(data)

    with open('./static/genres.json', 'w', encoding='utf-8') as f:
        data = "genres = '"
        f.write(data)
    with open('./static/genres.json', 'a', encoding='utf-8') as f:
        json.dump(genres, f)
    with open('./static/genres.json', 'a', encoding='utf-8') as f:
        data = "';"
        f.write(data)
