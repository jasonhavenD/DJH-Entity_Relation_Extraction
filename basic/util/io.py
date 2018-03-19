#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:io
   Author:jason
   date:2018/3/19
-------------------------------------------------
   Change Activity:2018/3/19:
-------------------------------------------------
"""
import codecs


class IOUtil():
	@staticmethod
	def load_files(files):
		'''
		:param files:文件列表
		:return:文件内容
		'''
		text = []
		print('reading files:', files)
		for file in files:
			if file:
				with codecs.open(file, 'rb', encoding='utf-8') as f:
					text.extend(f.readlines())
		return text
	
	@staticmethod
	def save_to_file(content, save_file):
		# 保存到文件
		print('saving file:', save_file)
		with codecs.open(save_file, 'w', encoding='utf-8') as f:
			for line in content:
				f.write(line)
