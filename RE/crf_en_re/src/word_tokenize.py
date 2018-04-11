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
	input = "../data/sents/sents1.txt.utf-8"
	output = "../data/tokens/tokens1.txt.utf-8"

	sents = []
	with open(input, 'r', encoding='utf-8') as f:
		sents = f.readlines()

	tokenses = []
	for sent in sents:
		tokenses.append(nltk.word_tokenize(sent))

	with open(output, 'w', encoding='utf-8') as f:
		for tokens in tokenses:
			f.write(' '.join(tokens))
			f.write("\n")
