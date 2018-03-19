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


# 检查某字符是否分句标志符号
def FindToken(char, cutlist):
	if char in cutlist:
		return True
	else:
		return False


# 进行分句
def Cut(lines, cutlist):
	'''
	:param lines: 待切分多行句子文本
	:param cutlist: 切分符号集合
	:return:
	'''
	l = []  # 句子列表，分句后的整句内容
	temp = []  # 临时列表，用于存储捕获到分句标志符之前的每个字符，一旦发现分句符号后，就会将其内容全部赋给l，然后就会被清空
	
	for line in lines:
		if FindToken(line, cutlist):  # 如果当前字符是分句符号
			temp.append(line)  # 将此字符放入临时列表中
			l.append(''.join(temp))  # 并把当前临时列表的内容加入到句子列表中
			temp = []
		else:  # 如果当前字符不是分句符号，则将该字符直接放入临时列表中
			temp.append(line)
	return l


if __name__ == '__main__':
	input = '0original.utf-8'
	text = IOUtil.load_files([input])
	# print(text)
	
	sents = []
	
	# 设置分句的标志符号
	cutlist = "。！？"
	
	for lines in text:
		l = Cut(list(lines), list(cutlist))
		for line in l:
			if line.strip() != "":
				sents.append(line)
				sents.append('\n')
	IOUtil.save_to_file(sents, 'sentences.utf-8')
