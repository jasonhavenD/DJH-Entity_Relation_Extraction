#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:trans2utf8
   Author:admin
   date:2018/4/11
-------------------------------------------------
   Change Activity:2018/4/11:
-------------------------------------------------
"""
import codecs
import os
import chardet

convertfiletypes = [
	".txt",
]


def convert_encoding(filename, target_encoding):
	content = codecs.open(filename, 'r').read()
	codecs.open(filename + ".utf-8", 'w', encoding=target_encoding).write(content)
	print("file:'{}' has been converted from to utf-8 !".format(filename))


def main(convertdir):
	for root, dirs, files in os.walk(convertdir):
		for f in files:
			for filetype in convertfiletypes:
				if f.lower().endswith(filetype):
					filename = os.path.join(root, f)
					try:
						convert_encoding(filename, 'utf-8')
					except Exception as e:
						print("'{}' cause a exception!".format(filename), e)


if __name__ == '__main__':
	convertdir = "../data/"
	main(convertdir)
