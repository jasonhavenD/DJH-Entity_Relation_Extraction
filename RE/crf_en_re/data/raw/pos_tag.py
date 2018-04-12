#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:pos_tag
   Author:admin
   date:2018/4/12
-------------------------------------------------
   Change Activity:2018/4/12:
-------------------------------------------------
"""
from stanfordcorenlp import StanfordCoreNLP


def pos_tag(sents):
	nlp = StanfordCoreNLP("c:/stanford-corenlp-full-2018-02-27")
	tokenses = []
	for sent in sents:
		tokens = nlp.word_tokenize(sent)
		print(tokens)
		tokenses.append(tokens)
	nlp.close()
	return tokenses


delimiter = '\t'

if __name__ == '__main__':
	input = "raw1_sents.txt.utf-8"
	output = "raw1_tagged.txt.utf-8"

	sents = []
	with open(input, 'r', encoding='utf-8') as f:
		text = f.readlines()

	pos_tagged_tokenses = pos_tag(sents[0])

	with open(output, 'w', encoding='utf-8') as f:
		for tokens in pos_tagged_tokenses:
			f.write(' '.join(tokens))
			f.write("\n")
