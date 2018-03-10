#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
分词
-------------------------------------------------
   File Name:test
   Author:jason
   date:2018/3/9
-------------------------------------------------
   Change Activity:2018/3/9:
-------------------------------------------------
"""

import jieba


if __name__=='__main__':
    file="./data/original.txt"
    with open(file,'r') as f:
        content=f.read()
    word_segment_list=jieba.lcut(content,HMM=True,cut_all=False)
    print(word_segment_list)
