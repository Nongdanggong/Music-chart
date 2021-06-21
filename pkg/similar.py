#usr/bin/python3
#-*- coding: utf-8 -*-

import numpy
from flask import Flask, render_template

def cos_similarity(all_list,one_list,number):

        v_one=[]
        v_all=[]
        all = 1
        i = 1

        for key in all_list.keys():
                v_all.append(all)

                value = 0
                for one_key in one_list:
                        if (key==one_key):
                                value = 1
                v_one.append(value)
                i += 1
                if (i > number):
                        break

        #print(v_all)
        #print(v_one)

        x = numpy.dot(v_all,v_one)
        result = x / (numpy.linalg.norm(v_all) * numpy.linalg.norm(v_one))

        return result


