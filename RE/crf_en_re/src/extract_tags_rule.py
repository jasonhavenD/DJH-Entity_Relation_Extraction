#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:extract_tags
   Author:admin
   date:2018/4/11
-------------------------------------------------
   Change Activity:2018/4/11:
-------------------------------------------------
"""
import nltk
import re

if __name__ == '__main__':
	input = "../data/tagged/tagged1.txt.utf-8"
	output = "../data/tagged/tags_rule.txt"
	text = ""
	with open(input, 'r', encoding='utf-8') as f:
		text = f.read()
	pattern = re.compile("</(.+?)>")
	tags = sorted(set(t for t in re.findall(pattern, text)))
	with open(output, 'w', encoding='utf-8') as f:
		f.write('\t'.join(tags))
