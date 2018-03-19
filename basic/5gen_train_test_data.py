#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   生成训练数据和测试数据
   File Name:get_train_test_data
   Author:jason
   date:2018/3/19
-------------------------------------------------
   Change Activity:2018/3/19:
-------------------------------------------------
"""
import codecs
import random
import numpy as np
from util.io import IOUtil

if __name__ == '__main__':
	input = 'character_tags.utf-8'
	ftrain = 'data/train.utf-8'
	ftest = 'data/test.utf-8'
	text = IOUtil.load_files([input])
	# print(text)
	
	train_index = random.sample(range(len(text)), int(len(text) * 0.8))
	test_index = random.sample(range(len(text)), int(len(text) * 0.2))
	
	train = np.array(text)[train_index]
	test = np.array(text)[test_index]
	# print(len(train), len(test))
	
	IOUtil.save_to_file(train, '6crf++/train.utf-8')
	IOUtil.save_to_file(test, '6crf++/test.utf-8')
	
	IOUtil.save_to_file(train, ftrain)
	IOUtil.save_to_file(test, ftest)
