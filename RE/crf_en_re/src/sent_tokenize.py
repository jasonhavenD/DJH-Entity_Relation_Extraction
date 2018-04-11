#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:sent_tokenize
   Author:admin
   date:2018/4/11
-------------------------------------------------
   Change Activity:2018/4/11:
-------------------------------------------------
"""
import nltk

if __name__ == '__main__':
	input = "../data/raw/raw1.txt.utf-8"
	output = "../data/sents/sents1.txt.utf-8"

	text = ""
	with open(input, 'r', encoding='utf-8') as f:
		text = f.read()
	sents = nltk.sent_tokenize(text)

	with open(output, 'w', encoding='utf-8') as f:
		f.writelines('\n'.join(sents))
