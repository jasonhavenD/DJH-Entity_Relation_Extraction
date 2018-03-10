#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
提取关键字使用自定义IDF语料
关键词提取所使用逆向文件频率（IDF）文本语料库可以切换成自定义语料库的路径
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
    USAGE="usage:    python user_idf.py [file name] -k [top k]"
    parser=OptionParser(USAGE)
    parser.add_option("-k",dest="topK")
    opt,args=parser.parse_args()
    
    if len(args)<1:
        print(USAGE)
        sys.exit()
    file_name=args[0]
    
    if opt.topK is None:
        topK=10
    else:
        topK=int(opt.topK)
    
    with open(file_name,'r') as f:
        content=f.read()
    
    print('file :',file_name)
    print('topK :',topK)
    
    jieba.analyse.set_idf_path('./idf/myidf.txt')
    keywords = jieba.analyse.extract_tags(content, topK=topK)
    
    print(','.join(keywords))
    