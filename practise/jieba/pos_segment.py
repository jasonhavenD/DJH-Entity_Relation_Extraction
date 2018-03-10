#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
词性标注
-------------------------------------------------
   File Name:test
   Author:jason
   date:2018/3/9
-------------------------------------------------
   Change Activity:2018/3/9:
-------------------------------------------------
"""

import jieba
import jieba.posseg as pseg


if __name__=='__main__':
    file="./data/original.txt"
    with open(file,'r') as f:
        content=f.read()
    words = pseg.cut(content)
    for word,flag in words:
        print('%s %s' % (word, flag))
    
    
    
