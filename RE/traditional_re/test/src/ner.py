#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:ner
   Author:jason
   date:2018/3/19
-------------------------------------------------
   Change Activity:2018/3/19:
-------------------------------------------------

"""

from stanfordcorenlp import StanfordCoreNLP
from util.io import IOUtil

if __name__ == '__main__':
	train_input = 'corpora/bakeoff2005/data/mypku_training.utf-8'
	test_input = 'corpora/bakeoff2005/data/mypku_test.utf-8'
	
	train_words = IOUtil.load_files([train_input])
	test_words = IOUtil.load_files([test_input])
	
	nlp = StanfordCoreNLP('C:\stanford-corenlp-full-2018-02-27', lang='zh')
	
	'''
	train_words_pos_taged = []
	for line in train_words:
		if line.strip() == '':
			continue
		line_tags = nlp.pos_tag(line)
		for pos_tag in line_tags:
			train_words_pos_taged.append(' '.join(pos_tag))
			train_words_pos_taged.append('\n')
	# print(train_words_pos_taged)
	
	test_words_pos_taged = []
	for line in test_words:
		if line.strip() == '':
			continue
		line_tags = nlp.pos_tag(line)
		for pos_tag in line_tags:
			test_words_pos_taged.append(' '.join(pos_tag))
			test_words_pos_taged.append('\n')
	# print(test_words_pos_taged)
	'''
	
	print(nlp.ner('我是代江海'))
	
	# train_output = 'output/train_words_pos_taged.utf-8'
	# test_output = 'output/test_words_pos_taged.utf-8'
	# IOUtil.save_to_file(train_words_pos_taged, train_output)
	# IOUtil.save_to_file(test_words_pos_taged, test_output)
	
	nlp.close()
