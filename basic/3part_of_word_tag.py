#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   Author:jason
   date:2018/3/17
-------------------------------------------------
   Change Activity:2018/3/17:
-------------------------------------------------
"""

from stanfordcorenlp import StanfordCoreNLP
from util.io import IOUtil

delimiter = ' '

if __name__ == '__main__':
	input = 'words.utf-8'
	text = IOUtil.load_files([input])
	# print(text)
	
	postags = []
	
	nlp = StanfordCoreNLP('http://corenlp.run', port=80, lang='zh')
	
	for line in text:
		l = nlp.pos_tag(line)
		for tlp in l:
			word, tag = tlp
			postags.append(str(word) + delimiter + str(tag) + '\n')
		postags.append('\n')
	nlp.close()
	IOUtil.save_to_file(postags, 'postags.utf-8')
