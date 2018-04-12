#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:convert2input
   Author:jason
   date:2018/4/11
-------------------------------------------------
   Change Activity:2018/4/11:
-------------------------------------------------
"""
import codecs

delimiter = '\t'
if __name__ == '__main__':
	inputs = ["../data/tokens/tokens1.txt.utf-8", "../data/tagged/tokens1_tagged.txt.utf-8",
	          "../data/nered/nered1.txt.utf-8", "../data/dependency/dependency1.txt.utf-8"]
	output = "../data/input/input1.txt.utf-8"

	tokenses = codecs.open(inputs[0], 'r', encoding='utf-8').readlines()
	taggedes = codecs.open(inputs[1], 'r', encoding='utf-8').readlines()
	neredes = codecs.open(inputs[2], 'r', encoding='utf-8').readlines()
	dependencies = codecs.open(inputs[3], 'r', encoding='utf-8').readlines()

	content = []

	for tokens, tags, ners, deps in zip(tokenses[:2], taggedes[:2], neredes[:2], dependencies[:2]):
		for token, tag, ner, dep in zip(tokens.strip().split(), tags.strip().split(delimiter),ners.strip().split(delimiter), deps.strip().split(delimiter)):
			content.append((token, tag.split('/')[1], ner.split('/')[1], dep.split('/')[1], dep.split('/')[2]))
		content.append('')

	with open(output, 'w', encoding='utf-8') as f:
		for item in content:
			f.write(delimiter.join(item))
			f.write('\n')
