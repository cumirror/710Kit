# !/usr/bin/env python
# encoding: utf-8
# code by 710
from socket import gethostbyname,socket,AF_INET,SOCK_STREAM
from urlparse import urlparse
from threading import Thread,Lock
import Queue
import time

threadLock = Lock()

class portScan(Thread):
	def __init__(self, host, port,result_file):
		Thread.__init__(self)
		self.host_list = host
		self.port = port
		self.result = result_file

	def run(self):
		while True:
			if self.host_list.empty():
				break
			url = urlparse(self.host_list.get())
			ip = url.netloc
			if ip == '':
				ip = self.host_list.get()
			#print ip
			s = socket(AF_INET,SOCK_STREAM)
			#print "%s of %s" % (self.port,ip)
			try:
				s.settimeout(3)
				s.connect((ip,self.port))
				print "%s of %s is open" % (self.port,ip)
				threadLock.acquire()
				self.result.write(ip+"\n")
				threadLock.release()
				
			except:
				print "%s error" % ip
			
def port_scan(port):
	result_file = openfile('../dict/port_result')
	result_file.write("the websites of %s is open:\n" % port)
	jobs = Queue.Queue(0)
	for url in open('../dict/urls'):
		jobs.put(url.rstrip()) 	#將文本加入到队列中
	for x in range(20): 		#创建20个线程
		t = portScan(jobs,port,result_file).start()
		#time.sleep(1)
	return True
def openfile(filename):
	f = open(filename,'w')
	return f

port_scan(80)
