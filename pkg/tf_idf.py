#!/usr/bin/python3
#-*- coding: utf-8 -*-

def tf_idf(all_list, number):
	g_list = {}
	i = 1

	for g in all_list.keys():
		if all_list[g][5] not in g_list.keys():
			g_list[all_list[g][5]]=0
		g_list[all_list[g][5]] +=1
		
		i += 1
		if ( i > number ) :
			break

	for key in g_list.keys():
		g_list[key] = g_list[key]/float(number)

	g_lists = sorted(g_list.items(), key=lambda x:x[1], reverse=True)

	return g_lists

