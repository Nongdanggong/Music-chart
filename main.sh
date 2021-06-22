#!/bin/bash

#sudo apt-get install python3-pip
#sudo pip install flask

# 유튜브 api를 위한 모듈
pip3 install apiclient
pip3 install oauth2client
pip3 install google-api-python-client
pip3 install google-api-core
pip3 install google-auth
pip3 install google-auth-httplib2
pip3 install google-auth-oauthlib
pip3 install googleapis-common-protos
pip3 install elasticsearch_dsl

chmod +x app.py
#nohup ./app.py --listen-port=8899 &
./app.py --listen-port=8899

sleep 2

firefox http://127.0.0.1:8899/


