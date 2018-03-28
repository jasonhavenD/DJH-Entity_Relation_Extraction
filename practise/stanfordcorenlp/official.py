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
import codecs
import os
from stanfordcorenlp import StanfordCoreNLP
import json

if __name__ == '__main__':
	chinese_sents = '''
	最满意的一点：空间够大，配置够全，动力够劲？最不满意的一点：刚上市，终端没有优惠
	'''
	english_sents = '''
	stanfordcorenlp is a Python wrapper for Stanford CoreNLP. It provides a simple API for text processing tasks such as Tokenization, Part of Speech Tagging, Named Entity Reconigtion, Constituency Parsing, Dependency Parsing, and more.
	'''
	
	'''
	#简单使用例子
	
	nlp = StanfordCoreNLP(r'C:\stanford-corenlp-full-2018-02-27')
	sentence = 'Guangdong University of Foreign Studies is located in Guangzhou.'
	print('Tokenize:', nlp.word_tokenize(sentence))
	print('Part of Speech:', nlp.pos_tag(sentence))
	print('Named Entities:', nlp.ner(sentence))
	print('Constituency Parsing:', nlp.parse(sentence))
	print('Dependency Parsing:', nlp.dependency_parse(sentence))
	nlp.close()  # Do not forget to close! The backend server will consume a lot memery.
	
	'''
	# 使用已存在的服务
	nlp = StanfordCoreNLP('http://corenlp.run', port=80)
	# nlp = StanfordCoreNLP(r'C:\stanford-corenlp-full-2018-02-27')
	
	# General API
	'''
	annotators: tokenize, ssplit, pos, lemma, ner, parse, depparse, dcoref (See Detail)
	pipelineLanguage: en, zh, ar, fr, de, es (English, Chinese, Arabic, French, German, Spanish) (See Annotator Support Detail)
	outputFormat: json, xml, text
	'''
	# props = {'annotators': 'tokenize,ssplit,pos', 'pipelineLanguage': 'en', 'outputFormat': 'json'}
	# print(nlp.annotate(english_sents, properties=props))
	
	# nlp.switch_language('zh')
	# output = nlp.annotate(chinese_sents, {'annotators': 'tokenize,ssplit', 'outputFormat': 'json'})
	# text = nlp.annotate(chinese_sents, {'annotators': 'tokenize,ssplit', 'outputFormat': 'text'})
	# print(output)
	# print(type(output))
	# print(os.getcwd())
	# output_dict = json.loads(output, encoding='utf-8')
	# print(output_dict)
	# with codecs.open('output.json', 'w', 'utf-8') as f:
	# 	json.dump(output_dict, f)
	nlp.close()
