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

if __name__ == '__main__':
	input = 'sentences.utf-8'
	text = IOUtil.load_files([input])
	# print(text)
	
	words = []
	
	nlp = StanfordCoreNLP('http://corenlp.run', port=80, lang='zh')
	
	for line in text:
		l = nlp.word_tokenize(line)
		words.extend(' '.join(l))
		words.append('\n')
	nlp.close()
	IOUtil.save_to_file(words, 'words.utf-8')
