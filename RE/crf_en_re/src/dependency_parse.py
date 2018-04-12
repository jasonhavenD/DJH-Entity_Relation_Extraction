#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:depandency
   Author:admin
   date:2018/4/12
-------------------------------------------------
   Change Activity:2018/4/12:
-------------------------------------------------
"""
from stanfordcorenlp import StanfordCoreNLP

if __name__ == '__main__':
	input = "../data/sents/sents1.txt.utf-8"
	output = "../data/dependency/dependency1.txt.utf-8"

	nlp = StanfordCoreNLP("c:/stanford-corenlp-full-2018-02-27")

	sents = []
	with open(input, 'r', encoding='utf-8') as f:
		sents = f.readlines()

	rst = [nlp.dependency_parse(sent) for sent in sents]

	with open(output, 'w', encoding='utf-8') as f:
		for sent in rst:
			for dep, pre, cur in sent:
				f.write("{}/{}/{}\t".format(cur, pre, dep))
		f.write('\n')

	nlp.close()
