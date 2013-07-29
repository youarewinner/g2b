#! /usr/bin/python2 
# -*- encoding: utf-8 -*-
# 유닉스의 경우에,  cgi 스크립트를 실행하기 위해서는 현재 파일을 chmod +x 로 실행가능비트로 지정하고 #! /usr/bin/python2와 같이 경로를 지정한다. 
# windows에서는 이런게 필요없다.
# python 2.4.3
# Beautiful Soup (3.2.1)
import codecs
import sys
import re
import urllib
from BeautifulSoup import BeautifulSoup

#streamWriter = codecs.lookup('utf-8')[-1]
#sys.stdout = streamWriter(sys.stdout)

html_source = urllib.urlopen('http://www.dreamline.kr/dreamline-blog').read()
soup = BeautifulSoup(html_source, fromEncoding="utf-8")

print soup.title

#for link in soup.findAll('a'):
#    print(link.get('href'))
#	print soup.get_text()

paraText = soup.find(text='Home')

print paraText

print paraText.findNextSiblings('a')
print paraText.next

#print soup.findAll('p', limit=1)

# 출력할 대상을 제한할 때 limit 이 필요함
print soup('a',limit=2)

#python에서 한글만 추출하는 방법

words = re.findall(u'[\uAC00-\uD7A3]+', html_source)
print words


