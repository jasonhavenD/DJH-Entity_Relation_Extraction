#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:8entity_pair_retract
   Author:jason
   date:2018/3/19
-------------------------------------------------
   Change Activity:2018/3/19:
-------------------------------------------------
"""
import codecs

delimiter = '\t'

if __name__ == '__main__':
	file = '6crf++/result.txt'
	entities = []
	pair = []
	with codecs.open(file, 'r', encoding='utf-8') as f:
		for line in f.readlines():
			if len(line.strip()) == 0:
				entities.append(pair)
				pair = []
				continue
			split = line.split(delimiter)
			if len(split) == 4:
				if split[3].strip() != 'O':
					pair.append(split[3])
	for pair in entities:
		print(pair)
