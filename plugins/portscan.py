# !/usr/bin/env python
# encoding: utf-8
# by 710
from socket import gethostbyname,socket,AF_INET,SOCK_STREAM
from threading import Thread
import Queue
import time

class portScan(Thread):
	def __init__(self, host, port):
		Thread.__init__(self)
		self.host_list = host
		self.port = port

	def run(self):
		while True:
			if self.host_list.empty():
				break
			ip = self.host_list.get()
			s = socket(AF_INET,SOCK_STREAM)
			#print "%s of %s" % (self.port,ip)
			try:
				s.settimeout(3)
				s.connect((ip,self.port))
				print "%s of %s is open" % (self.port,ip)
			except:
				print "%s error" % ip
			
def port_scan(port):
	jobs = Queue.Queue(0)
	for url in open('../dict/urls'):
		jobs.put(url.rstrip()) #將文本加入到队列中
	for x in range(10): #创建10个线程
		t = portScan(jobs,port).start()
		time.sleep(1)
	return True
port_scan(80)
