#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:script
   Author:admin
   date:2018/3/28
-------------------------------------------------
   Change Activity:2018/3/28:
-------------------------------------------------
"""
if __name__ == '__main__':
	file = "test.data"
	text = []
	with open(file, "r", encoding="utf-8") as f:
		for line in f.readlines():
			if line.strip() != "" and len(line.split()) != 3:
				continue
			text.append(line)
	with open(file, "w", encoding="utf-8") as f:
		f.writelines(text)
