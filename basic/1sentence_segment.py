#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   Author:jason
   date:2018/3/17
-------------------------------------------------
   Change Activity:2018/3/17:
-------------------------------------------------
"""
import codecs
from stanfordcorenlp import StanfordCoreNLP


class IOUtil():
	@staticmethod
	def load_files(files):
		'''
		:param files:文件列表
		:return:文件内容
		'''
		text = []
		print(files)
		for file in files:
			if file:
				with codecs.open(file, 'rb', encoding='utf-8') as f:
					text.extend(f.readlines())
		return text
	
	@staticmethod
	def save_to_file(result_text, save_file):
		# 保存到文件
		with codecs.open(save_file, 'w', encoding='utf-8') as f:
			for line in result_text:
				for token in line:
					f.write(token.replace('/', '\t') + '\n')  # 注意保存时用tab分隔符
				f.write('\n')


if __name__ == '__main__':
	input = '0original.utf-8'
	text = IOUtil.load_files([input])
	# print(input_data)
	
	# use an existing server
	nlp = StanfordCoreNLP('http://corenlp.run', port=80)
	sents = []
	for line in text:
		pros = {}
		json = nlp.annotate(line, pros)
		sents.append('')
	nlp.close()
