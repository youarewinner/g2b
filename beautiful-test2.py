# -*- encoding : utf-8 -*-

from BeautifulSoup import BeautifulSoup
import urllib2

url = 'http://www.naver.com'
handle = urllib2.urlopen(url)
data = handle.read()

soup = BeautifulSoup(data)
gnb = str( soup('div', {'class':'gnb',}) ) #div내의 tit class 추출
#print article.decode('utf8')
print gnb