#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:dependency
   Author:admin
   date:2018/3/29
-------------------------------------------------
   Change Activity:2018/3/29:
-------------------------------------------------
"""

from stanfordcorenlp import StanfordCoreNLP
from util.io import IOUtil
import datetime

if __name__ == '__main__':
	train_input = 'corpora/bakeoff2005/data/mypku_training.utf-8'
	test_input = 'corpora/bakeoff2005/data/mypku_test.utf-8'

	train_words = IOUtil.load_files([train_input])
	# test_words = IOUtil.load_files([test_input])

	nlp = StanfordCoreNLP('C:\stanford-corenlp-full-2018-02-27', lang='zh')

	begin = datetime.datetime.now()

	train_words_ner = []
	for line in train_words:
		if line.strip() == '':
			continue
		line_tags = nlp.dependency_parse(line)
		for tag in line_tags:
			print(type(tag), tag)
	# 	train_words_ner.append(' '.join(pos_tag))
	# 	train_words_ner.append('\n')
	# print(train_words_ner)

	# test_words_ner = []
	# for line in test_words:
	# 	if line.strip() == '':
	# 		continue
	# 	line_tags = nlp.dependency_parse(line)
	# 	for pos_tag in line_tags:
	# 		test_words_ner.append(' '.join(pos_tag))
	# 		test_words_ner.append('\n')
	# # print(test_words_ner)
	#
	train_output = 'output/dependency_parse/train_words_dependency_parse.utf-8'
	# test_output = 'output/dependency_parse/test_words_dependency_parse.utf-8'
	IOUtil.save_to_file(train_words_ner, train_output)
	# IOUtil.save_to_file(test_words_ner, test_output)

	nlp.close()

	end = datetime.datetime.now()
	print('finished in ' + str((end - begin).seconds) + ' s!')
