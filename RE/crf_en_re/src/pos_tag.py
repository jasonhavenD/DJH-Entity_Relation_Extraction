#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:pos_tag
   Author:jason
   date:2018/4/11
-------------------------------------------------
   Change Activity:2018/4/11:
-------------------------------------------------
"""

import nltk

delimiter = '\t'

if __name__ == '__main__':
	input = "../data/tokens/tokens1.txt.utf-8"
	output = "../data/tagged/tokens1_tagged.txt.utf-8"

	tokenses = []
	with open(input, 'r', encoding='utf-8') as f:
		for tokens in f.readlines():
			tokenses.append(tokens.split())
	pos_tagged_tokenses = [nltk.pos_tag(tokens) for tokens in tokenses]

	with open(output, 'w', encoding='utf-8') as f:
		for pos_tag_tokens in pos_tagged_tokenses:
			for word_with_tag in pos_tag_tokens:
				f.write('/'.join(word_with_tag))
				f.write(delimiter)
			f.write("\n")
