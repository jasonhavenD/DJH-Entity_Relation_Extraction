#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:bioes2bio
   Author:admin
   date:2018/4/16
-------------------------------------------------
   Change Activity:2018/4/16:
-------------------------------------------------
"""


def bioes2bio(tags):
	new_tags = []
	for i, tag in enumerate(tags):
		if tag.split('-')[0] == 'B':
			new_tags.append(tag)
		elif tag.split('-')[0] == 'I':
			new_tags.append(tag)
		elif tag.split('-')[0] == 'S':
			new_tags.append(tag.replace('S-', 'B-'))
		elif tag.split('-')[0] == 'E':
			new_tags.append(tag.replace('E-', 'I-'))
		elif tag.split('-')[0] == 'O':
			new_tags.append(tag)
		else:
			raise Exception('Invalid format!')
	return new_tags

if __name__ == '__main__':
    pass