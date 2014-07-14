#!/usr/bin/env python
#encoding: utf-8
#code by zer0cloud

import sys,getopt
from lib import *

from plugins.sameip import same_ip
from plugins.subdomain import get_subdomain
from plugins.ftplogin import ftp_guess

def main():
	url = ''
	if len(sys.argv) < 4:
		usage()
		sys.exit()
	try:
		opts,args = getopt.getopt(sys.argv[1:],'t:sih',['help','ftp'])
	except getopt.GetoptError:
		usage()
		sys.exit()
	for c,v in opts:
		if c in ("-h"):
			usage()
			sys.exit()
		elif c in ("-t"):
			url = v
			if not is_url(url):
				print 'URL Error :('
				sys.exit()
		elif url == '':
			print 'Please enter target'
		elif c in ("-s"):
			domain = getdomain(url)
			if domain == False:
				print 'URL Error :(('
				sys.exit()
			get_subdomain(domain)
		elif c in ("-i"):
			same_ip(url)
		elif c in ("--ftp"):
			ftp_guess(url)
def usage():
	print '710kit.py	[-t][value][-s|-i|--ftp]\n'
	print 'e.g.'
	print '710kit.py	-t www.google.com -i\n'
	print 'optional argumens:'
	print '  -h,--help	Show this help message and exit'
	print '  -t		Enter the target like www.google.com'
	print '  -s		Get the subdomain'
	print '  -i		Get the domain of sameip'
	print '  --ftp		Ftp brute force'

if __name__=="__main__":
	main()
