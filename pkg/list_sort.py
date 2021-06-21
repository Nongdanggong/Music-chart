#usr/bin/python3
#-*- coding: utf-8 -*-

from flask import Flask, render_template

def list_sort(all_music):
        for key in all_music.keys():
                if(all_music[key][1]!=1):
                        all_music[key][0] = (all_music[key][0]/all_music[key][1])

        list={}
        i = 1
        for key, value in sorted(all_music.items(), key=lambda x:x[1]):
                list[key] = value
                list[key][1] = i
                i += 1


        return list

