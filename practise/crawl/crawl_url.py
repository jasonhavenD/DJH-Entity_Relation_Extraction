#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:crawl_url
   Author:jason
   date:2018/3/24
-------------------------------------------------
   Change Activity:2018/3/24:
-------------------------------------------------
"""
# coding:utf-8
from selenium import webdriver
import time

browser = webdriver.Chrome()
time.sleep(3)
browser.get('http://ent.sina.com.cn/film/')
time.sleep(2)
browser.maximize_window()
time.sleep(1)
js = "var q=document.documentElement.scrollTop=150000"
browser.execute_script(js)
time.sleep(1)
browser.execute_script(js)
time.sleep(1)
browser.execute_script(js)
time.sleep(1)

i = 1
urlfilename = './links/links' + str(i) + '.txt'
elem = browser.find_elements_by_class_name("feed-card-item")
fileurl = open(urlfilename, 'w', encoding="utf-8")
for w in range(len(elem)):
	elem_a = elem[w].find_element_by_tag_name("h2").find_elements_by_tag_name("a")
	print(elem_a[0].get_attribute("href"))
	fileurl.write(elem_a[0].get_attribute("href") + '\n')
fileurl.close()

xpathstr1 = "//*[@id='feedCardContent']/div[3]/span[7]/a"
xpathstr2 = "//*[@id='feedCardContent']/div[3]/span[8]/a"

while (i<7):
	if i <= 5:
		browser.find_element_by_xpath(xpathstr1).click()
		time.sleep(1)
	elif i <= 140:
		browser.find_element_by_xpath(xpathstr2).click()
		time.sleep(1)
	elif i > 140:
		browser.find_element_by_xpath(xpathstr1).click()
		time.sleep(1)
	
	browser.execute_script(js)
	time.sleep(1)
	browser.execute_script(js)
	time.sleep(1)
	browser.execute_script(js)
	time.sleep(1)
	
	i = i + 1
	urlfilename = './links/links' + str(i) + '.txt'
	elem = browser.find_elements_by_class_name("feed-card-item")
	fileurl = open(urlfilename, 'w', encoding="utf-8")
	for w in range(len(elem)):
		elem_a = elem[w].find_element_by_tag_name("h2").find_elements_by_tag_name("a")
		print(elem_a[0].get_attribute("href"))
		fileurl.write(elem_a[0].get_attribute("href") + '\n')
	fileurl.close()