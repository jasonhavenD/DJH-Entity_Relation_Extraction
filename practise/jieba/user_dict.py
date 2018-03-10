#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
使用自定义词典
词典格式和 dict.txt 一样，一个词占一行；每一行分三部分：词语、词频（可省略）、词性（可省略），用空格隔开，顺序不可颠倒。file_name 若为路径或二进制方式打开的文件，则文件必须为 UTF-8 编码。
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
    mydict="./dict/mydict.txt"
    with open(mydict,'r',encoding='utf-8') as f:
        content=f.read()
    print(content)

    test_sent = (
    "李小福是创新办主任也是云计算方面的专家; 什么是八一双鹿\n"
    "例如我输入一个带“韩玉赏鉴”的标题，在自定义词库中也增加了此词为N类\n"
    "「台中」正確應該不會被切開。mac上可分出「石墨烯」；此時又可以分出來凱特琳了。"
    )
    
    words=jieba.cut(test_sent)
    print("/".join(words))
    
    jieba.add_word('凱特琳')
    jieba.add_word('石墨烯')
    words=jieba.cut(test_sent)
    print("/".join(words))
    
    jieba.del_word('石墨烯')
    words=jieba.cut(test_sent)
    print("/".join(words))
    