#!/usr/bin/python3
#-*- coding: utf-8 -*-

import re
import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template
from pkg.crawling import *

all_music = {}

all_music, melon_list = melon()
all_music, bugs_list = bugs(all_music)
all_music, genie_list = genie(all_music)
#위 10개까지만 장르가 등록됩니다. (test용)
all_music = genre(all_music, 10)



print(all_music,'\n\n')
print(melon_list,'\n\n')
print(bugs_list, '\n\n')
print(genie_list, '\n\n')
