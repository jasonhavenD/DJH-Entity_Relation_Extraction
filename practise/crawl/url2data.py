#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:url2data
   Author:jason
   date:2018/3/24
-------------------------------------------------
   Change Activity:2018/3/24:
-------------------------------------------------
"""
from urllib import request
from bs4 import BeautifulSoup

import re
import os
import os.path
import json

headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36',
}
rootdir = "./links"  # 指明被遍历的文件夹
i = 1

for parent, dirnames, filenames in os.walk(rootdir):  # 三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
	for filename in filenames:  # 输出文件信息
		linkdir = os.path.join(parent, filename)  # 输出文件路径信息
		with open(linkdir, 'r', encoding="utf-8") as f:
			for url in f.readlines():
				print("current url:", url)
				
				datadic = {}
				
				if url.strip() == "":
					continue
				
				try:
					req = request.Request(url, headers=headers)
					resp = request.urlopen(req)
					if resp.status != 200:
						print('url open error!')
						continue
					
					html = resp.read()
					try:
						html = html.decode("utf-8")
					except UnicodeDecodeError as e:
						print("编码出错:", url)
						
					soup = BeautifulSoup(html, "lxml")
					
					titlestr = ""
					fromstr = ""
					articlestr = ""
					
					tilist = soup.find_all("h1")
					if len(tilist):  # 不空
						titlestr = str(tilist[0])  # 标题
					
					sourlist = soup.find_all("a", class_="source ent-source")
					if len(sourlist):
						fromstr = str(sourlist[0])  # 来源
					
					arlist = soup.find_all("div", id="artibody")
					if len(arlist):
						for z in range(len(arlist[0].find_all('p'))):
							articlestr = articlestr + str(arlist[0].find_all('p')[z])  # 正文
					
					soup_title = BeautifulSoup(titlestr, 'lxml')
					soup_from = BeautifulSoup(fromstr, 'lxml')
					soup_article = BeautifulSoup(articlestr, 'lxml')
					
					datadic['title'] = soup_title.get_text()
					datadic['from'] = soup_from.get_text()
					datadic['article'] = soup_article.get_text()
					
					print(datadic)
					filestr = "./raw_data/" + datadic['title'] + ".txt"
					
					if not (not datadic['title'].strip() and not datadic['from'].strip() and not datadic[
						'article'].strip()):
						with open(filestr, 'w', encoding='utf-8') as f:
							json.dump(datadic, f)
					i = i + 1
				except IOError as e:
					print("*** file open error", e)
