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

from util.io import IOUtil
import sklearn_crfsuite as crf

delimiter = ' '

if __name__ == '__main__':
	input = 'postags.utf-8'
	text = IOUtil.load_files([input])
	print(text)
	
	
