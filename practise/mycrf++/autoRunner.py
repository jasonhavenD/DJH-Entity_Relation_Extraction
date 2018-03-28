#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:auto_runner
   Author:admin
   date:2018/3/28
-------------------------------------------------
   Change Activity:2018/3/28:
-------------------------------------------------
"""
import os
import sys
import datetime
from optparse import OptionParser


def train(command):
	os.system(command)


def test(command):
	os.system(command)


def eval(command):
	os.system(command)


if __name__ == '__main__':
	usage = "usage: python auto_runner.py [-h][--help][-d][--dir]"
	parser = OptionParser(usage=usage)
	parser.add_option("-d", "--dir", dest="dir", metavar='directory',
	                  help="set the directory of files")
	options, args = parser.parse_args()
	if options.dir == None:
		print(usage)
		sys.exit(0)
	begin = datetime.datetime.now()

	train_data = options.dir + os.path.sep + "train.data"
	test_data = options.dir + os.path.sep + "test.data"
	template = options.dir + os.path.sep + "template"
	print(train_data)
	print(test_data)
	print(template)

	print("train model ......")
	command = "crf_learn -c 4.0 {0} {1} model -t >train.log".format(template, train_data)
	train(command)
	print("test model ......")
	command = "crf_test -m model {0} > result.txt".format(test_data)
	test(command)
	print("eval model ......")
	command = "python conlleval.py result.txt > eval.txt"
	eval(command)
	end = datetime.datetime.now()
	print("finished in {0}s".format(end - begin))
