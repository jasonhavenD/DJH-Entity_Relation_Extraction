#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:bio
   Author:admin
   date:2018/4/16
-------------------------------------------------
   Change Activity:2018/4/16:
-------------------------------------------------
"""


def bio2bioes(tags):
	new_tags = []
	for i, tag in enumerate(tags):
		if tag == 'O':
			new_tags.append(tag)
		elif tag.split('-')[0] == 'B':
			if i + 1 != len(tags) and \
					tags[i + 1].split('-')[0] == 'I':
				new_tags.append(tag)
			else:
				new_tags.append(tag.replace('B-', 'S-'))
		elif tag.split('-')[0] == 'I':
			if i + 1 < len(tags) and \
					tags[i + 1].split('-')[0] == 'I':
				new_tags.append(tag)
			else:
				new_tags.append(tag.replace('I-', 'E-'))
		else:
			raise Exception('Invalid IOB format!')
	return new_tags


if __name__ == '__main__':
	pass
