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
from json import JSONDecodeError

from stanfordcorenlp import StanfordCoreNLP
from util.io import IOUtil

delimiter = ' '

if __name__ == '__main__':
	input = 'postags.utf-8'
	text = IOUtil.load_files([input])
	# print(text)
	
	character_tags = []
	
	# nlp = StanfordCoreNLP('http://corenlp.run', port=80, lang='zh')
	nlp = StanfordCoreNLP('C:\stanford-corenlp-full-2018-02-27', port=80, lang='zh')
	try:
		for line in text:
			if len(line.strip()) != 0:
				word, tag = line.strip().split(delimiter)
				print(word)
				character_tag = nlp.ner(word)
				print('ok')
				character_tags.append(word + delimiter + tag + delimiter + character_tag[0][1] + '\n')
			else:
				character_tags.append('\n')
	except JSONDecodeError as e:
		print('JSONDecodeError')
	except ConnectionError as e:
		print('ConnectionError')
	except Exception as e:
		print('something wrong happend!')
	nlp.close()
	IOUtil.save_to_file(character_tags, 'character_tags.utf-8')
