
curl -H 'Content-Type: application/json' -XGET http://localhost:9200/_count?pretty

#echo -e "\n\n all_musics"

curl --silent -XGET localhost:9200/all_musics/_search?q=Butter

echo -e "\n\n melon"

curl --silent -XGET localhost:9200/melon/_search?q=Butter

echo -e "\n\n bugs"

curl --silent -XGET localhost:9200/bugs/_search?q=Butter

echo -e "\n\n genie"

curl --silent -XGET localhost:9200/genie/_search?q=Butter

#curl --silent -XGET localhost:9200/test/_search?q=


#테스트 할 때 삭제 코드
#curl -XDELETE localhost:9200/*

#사이트
#http://localhost:9200/python3elasticsearch/log/_search
