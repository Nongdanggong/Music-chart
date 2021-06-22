#!/bin/python3
#-*- coding: utf-8 -*-

import json
import re

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
            for k in range(4):
                genre = {"genre" : json_data['_source'][i][k].split(' --> ')[0], "ratio" : json_data['_source'][i][k].split(' --> ')[1]}
                genres.append(genre)
            break
        rank = {"title" : re.sub("\'","\u2032", i), "singer" : json_data['_source'][i][2]}
        ranks.append(rank)


#    print(ranks)
#    print(genres)

    with open('./templates/ranks.json', 'w', encoding = 'utf-8') as f:
        data = "ranks = '"
        f.write(data)
    f.close()
    with open('./templates/ranks.json', 'a', encoding='utf-8') as f:
        json.dump(ranks, f)
    with open('./templates/ranks.json', 'a', encoding='utf-8') as f:
        data = "';"
        f.write(data)
    f.close()

    with open('./templates/genres.json', 'w', encoding='utf-8') as f:
        data = "genres = '"
        f.write(data)
    f.close()
    with open('./templates/genres.json', 'a', encoding='utf-8') as f:
        json.dump(genres, f)
    with open('./templates/genres.json', 'a', encoding='utf-8') as f:
        data = "';"
        f.write(data)
    f.close()
