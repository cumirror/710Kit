#!/usr/bin/env python
#encoding: utf-8
#code by 710

#add methods:
#	get_sub_of_chinaz  ---- not available now
#	try_sub_by_dns     ---- you need a dict
#by cumirror 2014/10/21

import re
import requests
import bs4
from bs4 import BeautifulSoup
import socket

def get_ip_from_subdomain(url):
        try:
            ip = socket.gethostbyname(url)
            return ip
        except socket.gaierror:
            return ""

def get_result(url):
        return url + ',' + get_ip_from_subdomain(url)

def get_sub_of_links(url):
	print("links-------")
	result = []
	source = requests.get('http://i.links.cn/subdomain/'+ url +'.html')
	#print(source.text)
	links = re.findall(r'(value="http://)([^>]+?)(">)',source.text)
	for link in links:
		domain = link[1].split('/')
		result.append(get_result(domain[0]))
		#print(domain[0])
	return result

#not available now
def get_sub_of_chinaz(url):
	print("chinaz-------")
	result = []
	payload = 's=' + url
	source = requests.post("http://s.tool.chinaz.com/same",data=payload)
	print(source.text)
	links = re.findall(r'(a herf=\'http://)([^\']+?)(\')',source.text)
	for link in links:
		domain = link[1].split('/')
		result.append(get_result(domain[0]))
		#print(domain[0])
	return result
	
def get_sub_of_baidu(url,page):
	print("Baidu-------")
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
			result.append(get_result(domain[0]))
			#print(domain[0])
		i = i+1
	return result
	
def get_sub_of_bing(url,page):
	print("bing-----")
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
			result.append(get_result(domain[0]))
			#print(domain[0])
		i = i+1
	return result

def try_sub_by_dns(url):
    print("DNS-----")
    sub_domain = open('dict.txt', 'rb')
    result = []
    for line in sub_domain:
        new_url = line.decode('utf-8').strip('\r\n') + '.' + url
        result.append(get_result(new_url))
        #print(new_url)
    return result

def get_subdomain(url):	
	'''
	查询网站子域名
	'''
	results = open('result.txt','w+')
	link1 = get_sub_of_links(url)
	link2 = get_sub_of_baidu(url,5)
	link3 = get_sub_of_bing(url,10)
	link4 = try_sub_by_dns(url)
	links = link1 + link2 + link3 + link4
	links = list(set(links))
	for link in links:
		#print(link)
		link = link + '\n'
		results.write(link)
	results.close()
