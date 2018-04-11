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
from nltk import pos_tag
from nltk.chunk import conlltags2tree,tree2conllstr
from nltk.tree import Tree

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


ne_tagged_sent = [('Rami', 'PERSON'), ('Eid', 'PERSON'), ('is', 'O'),
                  ('studying', 'O'), ('at', 'O'), ('Stony', 'ORGANIZATION'),
                  ('Brook', 'ORGANIZATION'), ('University', 'ORGANIZATION'),
                  ('in', 'O'), ('NY', 'LOCATION')]

ne_tree = stanfordNE2tree(ne_tagged_sent)
print(ne_tree)
print(tree2conllstr(ne_tree))
print(stanfordNE2BIO(ne_tagged_sent))