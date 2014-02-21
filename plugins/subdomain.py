#!/usr/bin/env python
#encoding: utf-8
#code by zer0cloud

import requests
from BeautifulSoup import BeautifulSoup

def get_subdomain(url):	
	'''
	查询网站子域名
	'''
	try:
		results = open('dict/domain','w+');
		source = requests.get('http://i.links.cn/subdomain/' + url + '.html')
		soup = BeautifulSoup(source.text)
		divs = soup.findAll("div","domain")

		if divs == []: #获取结果为空
			print 'Sorry,Nothing :('
		for div in divs:
			link = div.a.string + '\n'
			results.write(link)
		results.close()
		print 'the result is in dict :)'
	except:
		print '\nSome error!!'
		return True
