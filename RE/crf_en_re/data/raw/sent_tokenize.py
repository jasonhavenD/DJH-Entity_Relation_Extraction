#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:sent_tokenize
   Author:admin
   date:2018/4/12
-------------------------------------------------
   Change Activity:2018/4/12:
-------------------------------------------------
"""
import re
import nltk

'''
测试后发现用nltk 分句，斯坦福nlp分词，下面这种情况 标记的实体和标签链接不会被拆开
print(nltk.sent_tokenize("Textron_Systems_Canada_Inc._@ORG"))
print(nlp.word_tokenize("Textron_Systems_Canada_Inc._@ORG"))
'''


def convert2block(m):
	word_with_tag = (m.group(1), m.group(2))
	return "{}_@{}".format('_'.join(word_with_tag[0].split()), word_with_tag[1])


def pre_treat(text):
	pattern_of_tags = re.compile("<\w+?>(.+?)</(\w+?)>")
	# words_with_tag = re.findall(pattern_of_tags, text)
	# for word_with_tag in words_with_tag:
	# 	new_word = '@@'.join(('_'.join(word_with_tag[0].split()), word_with_tag[1]))
	# 	print(new_word)
	text = re.sub(pattern_of_tags, convert2block, text)
	return text


if __name__ == '__main__':
	input = "raw1_with_tag.txt.utf-8"
	output = "raw1_sents.txt.utf-8"

	text = ""
	with open(input, 'r', encoding='utf-8') as f:
		text = f.read()

	text = pre_treat(text)
	sents = nltk.sent_tokenize(text)

	print(len(sents))

	with open(output, 'w', encoding='utf-8') as f:
		f.writelines('\n'.join(sents))
