#!/usr/bin/env python
#encoding: utf-8
#code by 710

import re
import requests
from BeautifulSoup import BeautifulSoup

def get_subdomain(url):	
	'''
	查询网站子域名
	'''
	results = open('dict/domain','w+');

	link1 = get_sub_of_links(url)
	link2 = get_sub_of_baidu(url,5)
	link3 = get_sub_of_bing(url,10)
	links = link1 + link2 + link3
	links = list(set(links))
	for link in links:
		print link
		link = link + '\n'
		results.write(link)
	results.close()

def get_sub_of_links(url):
	print "links"
	result = []

	source = requests.get('http://i.links.cn/subdomain/'+ url +'.html')
	#print source.text
	links = re.findall(r'(value="http://)([^>]+?)(">)',source.text)
	for link in links:
		domain = link[1].split('/')
		result.append(domain[0])
		print domain[0]
	return result
	
def get_sub_of_baidu(url,page):
	print "Baidu-------"
	result = []
	i = 1
	while i <= page:
		num = i*100
		num = str(num)
		source = requests.get('http://www.baidu.com/s?rn=100&pn='+num+'&wd=site:'+ url)
		#print source.text
		links = re.findall(r'(<span class="g">)([^>]+?)(/&nbsp;)',source.text)
		for link in links:
			domain = link[1].split('/')
			result.append(domain[0])
			print domain[0]
		i = i+1
	return result
	
def get_sub_of_bing(url,page):
	print "bing-----"
	result = []
	i = 1
	while i < page:
		num = i*10
		num = str(num)
		source = requests.get('http://cn.bing.com/search?first='+num+'&q=site:'+url)
		#print source.text
		links = re.findall(r'("><h3><a href=")(.+?)(" target="_blank".+?>)',source.text)
		for link in links:
			temp = link[1].strip('http://')
			domain = temp.split('/')
			result.append(domain[0])
			print domain[0]
		i = i+1
	return result
