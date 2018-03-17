#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   功能：分词并做词性标注
   File Name:Pos_tag
   Author:jason
   date:2018/3/16
-------------------------------------------------
   Change Activity:2018/3/16:
-------------------------------------------------
"""
from stanfordcorenlp import StanfordCoreNLP

if __name__ == '__main__':
	nlp = StanfordCoreNLP(r'C:\stanford-corenlp-full-2018-02-27')
	sentence = '北京欢迎你！'
	# print('Tokenize:', nlp.word_tokenize(sentence))
	# print('Part of Speech:', nlp.pos_tag(sentence))
	# print('Named Entities:', nlp.ner(sentence))
	# print('Constituency Parsing:', nlp.parse(sentence))
	# print('Dependency Parsing:', nlp.dependency_parse(sentence))
	nlp.close() # Do not forget to close! The backend server will consume a lot memery.