#! /usr/bin/python2 
# -*- encoding: utf-8 -*-
# 유닉스의 경우에,  cgi 스크립트를 실행하기 위해서는 현재 파일을 chmod +x 로 실행가능비트로 지정하고 #! /usr/bin/python2와 같이 경로를 지정한다. 
# windows에서는 이런게 필요없다.
# div 내의 class가 gnb 인것을 추출한다.

from BeautifulSoup import BeautifulSoup
import urllib2

url = 'http://www.naver.com'
handle = urllib2.urlopen(url)
data = handle.read()

soup = BeautifulSoup(data)
gnb = str( soup('div', {'class':'gnb',}) ) # gnb in div
#print article.decode('utf8')
print gnb