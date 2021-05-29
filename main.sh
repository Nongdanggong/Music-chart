#!/bin/bash

#sudo apt-get install python3-pip
#sudo pip install flask

chmod +x app.py
./app.py --listen-port=8899

firefox http://127.0.0.1:8999/

#chmod +x kor_init.py
#./kor_init.py


