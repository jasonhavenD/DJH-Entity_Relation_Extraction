#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
基于 TextRank 算法的关键词抽取

-------------------------------------------------
   File Name:test
   Author:jason
   date:2018/3/9
-------------------------------------------------
   Change Activity:2018/3/9:
-------------------------------------------------
"""
import sys
import jieba
import jieba.analyse
from optparse import OptionParser


if __name__=='__main__':
    USAGE = "usage: python extract_tags_textrank.py [file name] -k [top k]"

    parser = OptionParser(USAGE)
    parser.add_option("-k", dest="topK")
    opt, args = parser.parse_args()


    if len(args) < 1:
        print(USAGE)
        sys.exit(1)
    print("args :",args)
    file_name = args[0]

    if opt.topK is None:
        topK = 10
    else:
        topK = int(opt.topK)
    
    with open(file_name,'r') as f:
        content=f.read()
    
    print('file :',file_name)
    print('topK :',topK)
    
    keywords = jieba.analyse.textrank(content, topK=topK)
    
    print(",".join(keywords))
    