#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:test
   Author:jason
   date:2018/4/11
-------------------------------------------------
   Change Activity:2018/4/11:
-------------------------------------------------
"""

import codecs
from stanfordcorenlp import StanfordCoreNLP
import re


if __name__ == '__main__':
	print("test")
	# input1 = "../data/sents/sents1.txt.utf-8"
	# input2 = "../data/raw/raw1_sents.txt.utf-8"
	# text1 = codecs.open(input1, 'r', encoding='utf-8').readlines()
	# text2 = codecs.open(input2, 'r', encoding='utf-8').readlines()
	#
	# print(len(text1),len(text2))
	#
	# i = 1
	# for sent1, sent2 in zip(text1, text2):
	# 	if sent1[:2] != sent2[:2]:
	# 		print(i, sent1)
	# 	i = i + 1


	# nlp = StanfordCoreNLP("c:/stanford-corenlp-full-2018-02-27")
	# sent="A joint study between Dr._Stephen_S._Fuller_of_George_Mason_University_@P1 and Chmura_Economics_and_Analytics_@ORG showed that America could lose an estimated 2.14 million jobs if Congress_@ORG does nothing to prevent the automatic sequestration cuts.But the effects of sequestration - on top of already reduced military spending on the president's watch - extend well-beyond our fragile economy."
	# tokens = nlp.word_tokenize(sent)
	# pattern_of_block = re.compile("^([\w.]+?_)+?@(\w+)$")
	# for token in tokens:
	# 	group = re.match(pattern_of_block, token)
	# 	if group:
	# 		print(token)
	# nlp.close()

	inputs = ["../data/tokens/tokens1.txt.utf-8", "../data/tagged/tokens1_tagged.txt.utf-8",
	          "../data/nered/nered1.txt.utf-8", "../data/dependency/dependency1.txt.utf-8",
	          "../data/raw/raw1_tagged.txt.utf-8"]

	output = "../data/input/input1.txt.utf-8"

	tokenses = codecs.open(inputs[0], 'r', encoding='utf-8').read()
	taggedes = codecs.open(inputs[1], 'r', encoding='utf-8').read()
	neredes = codecs.open(inputs[2], 'r', encoding='utf-8').read()
	dependencies = codecs.open(inputs[3], 'r', encoding='utf-8').read()
	targets = codecs.open(inputs[4], 'r', encoding='utf-8').read()

	print(len(tokenses.split()),len(taggedes.split()),len(neredes.split()),len(dependencies.split()),len(targets.split()))
