#!/usr/bin/python3
import sys 
import simplejson
from elasticsearch import Elasticsearch
from elasticsearch_dsl import Index


es_host="127.0.0.1"
es_port="9200"

es = Elasticsearch([{'host':es_host, 'port':es_port}])


test={"0X1=LOVESONG (I Know I Love You) feat. Seori" : [33, 31, '투모로우바이투게더', 'https://image.bugsm.co.kr/album/images/50/203998/20399866.jpg?version=20210601002859.0', 'https://www.youtube.com/results?search_query=0X1=LOVESONG (I Know I Love You) feat. Seori'], 
'Butter': [1.0, 1, '방탄소년단', 'https://cdnimg.melon.co.kr/cm2/album/images/106/12/483/10612483_20210521111412_500.jpg/melon/resize/120/quality/80/optimize', 'https://www.youtube.com/results?search_query=Butter'],
'LOVE DAY (2021) (바른연애 길잡이 X 양요섭, 정은지)': [42.666666666666664, 50, '양요섭', 'https://cdnimg.melon.co.kr/cm2/album/images/105/73/486/10573486_20210304202053_500.jpg/melon/resize/120/quality/80/optimize', 'https://www.youtube.com/results?search_query=LOVE DAY (2021) (바른연애 길잡이 X 양요섭, 정은지)'],
'ASAP': [10.333333333333334, 10, 'STAYC(스테이씨)', 'https://cdnimg.melon.co.kr/cm2/album/images/105/89/127/10589127_20210407175809_500.jpg/melon/resize/120/quality/80/optimize', 'https://www.youtube.com/results?search_query=ASAP']}


"""
test={"0X1=LOVESONG (I Know I Love You) feat. Seori" : [33, 31, '투모로우바이투게더'], 
'Butter': [1.0, 1, '방탄소년단'],
'LOVE DAY (2021) (바른연애 길잡이 X 양요섭, 정은지)': [42.6666666666664, 50, '양요섭'],
'ASAP': [10.33333333333334, 10, 'STAYC(스테이씨)']}
"""
#print(type(test))
#print(type(test["Butter"]))


for i in test.values():
#	print(i)
#	print(type(i[0]))
	i[0] = str(i[0])
#	print(type(i[0]))
	i[1] = str(i[1])


json_test = simplejson.dumps(test, ignore_nan = True)

if es.indices.exists(index="test"):
	es.indices.delete(index="test")


es.create(index='test', doc_type='test', id=5, body=json_test)
