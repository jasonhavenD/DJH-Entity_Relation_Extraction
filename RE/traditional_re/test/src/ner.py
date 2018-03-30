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
import datetime

if __name__ == '__main__':
	train_input = 'corpora/bakeoff2005/data/mypku_training.utf-8'
	test_input = 'corpora/bakeoff2005/data/mypku_test.utf-8'

	train_words = IOUtil.load_files([train_input])
	test_words = IOUtil.load_files([test_input])

	nlp = StanfordCoreNLP('C:\stanford-corenlp-full-2018-02-27', lang='zh')

	begin = datetime.datetime.now()

	train_words_ner = []
	for line in train_words:
		if line.strip() == '':
			continue
		line_tags = nlp.ner(line)
		for tag in line_tags:
			train_words_ner.append(' '.join(tag))
			train_words_ner.append('\n')
	# print(train_words_ner)

	test_words_ner = []
	for line in test_words:
		if line.strip() == '':
			continue
		line_tags = nlp.ner(line)
		for tag in line_tags:
			test_words_ner.append(' '.join(tag))
			test_words_ner.append('\n')
	# print(test_words_ner)

	train_output = 'output/ner/train_words_ner.utf-8'
	test_output = 'output/ner/test_words_ner.utf-8'
	IOUtil.save_to_file(train_words_ner, train_output)
	IOUtil.save_to_file(test_words_ner, test_output)

	nlp.close()

	end = datetime.datetime.now()
	print('finished in ' + str((end - begin).seconds) + ' s!')
