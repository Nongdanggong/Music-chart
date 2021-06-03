
curl -H 'Content-Type: application/json' -XGET http://localhost:9200/_count?pretty

echo -e "\n\n all_musics"

curl --silent -XGET localhost:9200/music_chart/_search?q=all_musics

echo -e "\n\n melon"

curl --silent -XGET localhost:9200/music_chart/_search?q=melon

echo -e "\n\n bugs"

curl --silent -XGET localhost:9200/music_chart/_search?q=bugs

echo -e "\n\n genie"

curl --silent -XGET localhost:9200/music_chart/_search?q=genie
