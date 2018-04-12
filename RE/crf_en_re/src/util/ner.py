#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:ner
   Author:admin
   date:2018/4/11
-------------------------------------------------
   Change Activity:2018/4/11:
-------------------------------------------------
"""
from nltk import pos_tag
from nltk.chunk import conlltags2tree, tree2conllstr
from stanfordcorenlp import StanfordCoreNLP


def stanfordNE2BIO(tagged_sent):
	bio_tagged_sent = []
	prev_tag = "O"
	for token, tag in tagged_sent:
		if tag == "O":  # O
			bio_tagged_sent.append((token, tag))
			prev_tag = tag
			continue
		if tag != "O" and prev_tag == "O":  # Begin NE
			bio_tagged_sent.append((token, "B-" + tag))
			prev_tag = tag
		elif prev_tag != "O" and prev_tag == tag:  # Inside NE
			bio_tagged_sent.append((token, "I-" + tag))
			prev_tag = tag
		elif prev_tag != "O" and prev_tag != tag:  # Adjacent NE
			bio_tagged_sent.append((token, "B-" + tag))
			prev_tag = tag
	
	return bio_tagged_sent


def stanfordNE2tree(ne_tagged_sent):
	bio_tagged_sent = stanfordNE2BIO(ne_tagged_sent)
	sent_tokens, sent_ne_tags = zip(*bio_tagged_sent)
	sent_pos_tags = [pos for token, pos in pos_tag(sent_tokens)]
	
	sent_conlltags = [(token, pos, ne) for token, pos, ne in zip(sent_tokens, sent_pos_tags, sent_ne_tags)]
	ne_tree = conlltags2tree(sent_conlltags)
	return ne_tree


def ner(sents, nlp):
	nered_sents = []
	for sent in sents:
		ner_sent = nlp.ner(sent)
		for word_with_tag in stanfordNE2BIO(ner_sent):
			nered_sents.append('/'.join(word_with_tag))
	return nered_sents


delimiter = '\t'

if __name__ == '__main__':
	input = "../data/sents/sents1.txt.utf-8"
	output = "../data/nered/nered1.txt.utf-8"
	
	nlp = StanfordCoreNLP("c:/stanford-corenlp-full-2018-02-27")
	
	sents = []
	with open(input, 'r', encoding='utf-8') as f:
		sents = f.readlines()
	
	with open(output, 'w', encoding='utf-8') as f:
		for sent in sents:
			ner_sent = nlp.ner(sent)
			for word_with_tag in stanfordNE2BIO(ner_sent):
				f.write('/'.join(word_with_tag))
				f.write(delimiter)
			f.write("\n")
	
	nlp.close()

# https://www.e-learn.cn/content/wangluowenzhang/168232
