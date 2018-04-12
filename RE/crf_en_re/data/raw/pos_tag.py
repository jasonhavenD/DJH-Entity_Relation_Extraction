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
import re

from stanfordcorenlp import StanfordCoreNLP


def pos_tag(sents):
	# sents = ["AM_General_@ORG, Lockheed_@ORG Martin, and Oshkosh_@ORG (pictured) are competing."]
	tokenses = []
	nlp = StanfordCoreNLP("c:/stanford-corenlp-full-2018-02-27")
	pattern_of_block = re.compile("^(\w+?_)+?@(\w+)$")
	for sent in sents:
		tokens = nlp.word_tokenize(sent)
		sent_with_tag = []
		for token in tokens:
			token_with_tag = token + "/O"
			group = re.match(pattern_of_block, token)
			if group:
				lst = []
				words_str, tag = group[0].split('@')
				if tag.endswith('>'):
					print(tag)
				# clean tag
				p = re.compile("\w+")
				tag = re.findall(p, tag)[0]
				# process words
				words_lst = words_str.strip().split('_')[:-1]
				for i, w in enumerate(words_lst):
					if i == 0:
						lst.append(w + '/B-' + tag)
					else:
						lst.append(w + '/I-' + tag)
				sent_with_tag.extend(lst)
				continue
			sent_with_tag.append(token_with_tag)
		tokenses.append(sent_with_tag)
	nlp.close()
	# print(len(tokenses))
	return tokenses


delimiter = '\t'

if __name__ == '__main__':
	input = "raw1_sents.txt.utf-8"
	output = "raw1_tagged.txt.utf-8"

	sents = []
	with open(input, 'r', encoding='utf-8') as f:
		sents = f.readlines()
	pos_tagged_tokenses = pos_tag(sents)

	#有点问题，解码不干净

	# with open(output, 'w', encoding='utf-8') as f:
	# 	for tokens in pos_tagged_tokenses:
	# 		f.write(delimiter.join(tokens))
	# 		f.write("\n")
