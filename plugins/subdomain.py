import requests
from BeautifulSoup import BeautifulSoup

def get_subdomain(url):	
	try:
		results = open('dict/domain','w+');
		source = requests.get('http://i.links.cn/subdomain/' + url + '.html')
		soup = BeautifulSoup(source.text)
		divs = soup.findAll("div","domain")
		#
		if divs == []:
			print 'Sorry,Nothing :('
		for div in divs:
			link = div.a.string + '\n'
			results.write(link)
		results.close()
		print 'the result is in dict :)'
	except:
		print '\nSome error!!.'
		return True
