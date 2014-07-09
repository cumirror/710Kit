import re
import requests

def is_url(url):
	regex = re.compile(
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
	return regex.search(url)
	
def getdomain(url):
	domain = url.split('.')
	domain = domain[-2]+'.'+domain[-1]
	print domain
	try:
		result = requests.get('http://'+domain)
		print result.status_code
		return domain
	except:
		return False
