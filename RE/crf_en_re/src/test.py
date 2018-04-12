#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:test
   Author:jason
   date:2018/4/11
-------------------------------------------------
   Change Activity:2018/4/11:
-------------------------------------------------
"""

import codecs

if __name__ == '__main__':
	input1 = "../data/sents/sents1.txt.utf-8"
	input2 = "../data/raw/raw1_sents.txt.utf-8"
	text1 = codecs.open(input1, 'r', encoding='utf-8').readlines()
	text2 = codecs.open(input2, 'r', encoding='utf-8').readlines()

	print(len(text1),len(text2))

	i = 1
	for sent1, sent2 in zip(text1, text2):
		if sent1[:2] != sent2[:2]:
			print(i, sent1)
		i = i + 1
