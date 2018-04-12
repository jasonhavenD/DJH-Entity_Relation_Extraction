#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:main
   Author:jason
   date:2018/4/12
-------------------------------------------------
   Change Activity:2018/4/12:
-------------------------------------------------
"""
from util import sent_tokenize, word_tokenize, pos_tag, dependency_parse, ner, merge2input_train
from stanfordcorenlp import StanfordCoreNLP
import codecs


def read(file):
	return codecs.open(file, 'r', encoding='utf-8').read()


def read_lst(file):
	return codecs.open(file, 'r', encoding='utf-8').readlines()


if __name__ == '__main__':
	nlp = StanfordCoreNLP("c:/stanford-corenlp-full-2018-02-27")
	# 1.准备数据
	# 1.1准备训练数据
	file_train_raw = "../data/raw/raw1_samples.txt.utf-8"  # samples
	train_raw = read(file_train_raw)
	train_sents = sent_tokenize.sent_tokenize(train_raw)
	train_nered_sents = ner.ner(train_sents, nlp)
	train_dependency_sents = dependency_parse.dependency_parse(train_sents, nlp)
	train_tokenses = word_tokenize.word_tokenize(train_sents, nlp)
	train_tagged_tokenses = pos_tag.pos_tag(train_tokenses)
	
	# 1.2准备测试数据
	
	# 2.训练模型
	
	# 3.测试模型
	
	# 4.评估模型
	
	# 5.预测
	
	nlp.close()
