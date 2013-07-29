#! /usr/bin/python2 
# -*- encoding: utf-8 -*-
# 유닉스의 경우에,  cgi 스크립트를 실행하기 위해서는 현재 파일을 chmod +x 로 실행가능비트로 지정하고 #! /usr/bin/python2와 같이 경로를 지정한다. 
# windows에서는 이런게 필요없다.
# python 2.4.3
import urllib2
import time


page = urllib2.urlopen('http://www.dreamline.kr/dreamline-blog/')
text = page.read()

where = text.find('드림라인')

print "드림라인 위치 : "
print where

while where < 50000 :
	time.sleep(5)
	where = text.find('드림라인')
	print "드림라인 위치 : "
	print where
	start_of_leasedline = where + 0
	end_of_leasedline = start_of_leasedline + 30
	leasedline = text[start_of_leasedline:end_of_leasedline]
	print (leasedline)
	
print "\n 끝났음"
