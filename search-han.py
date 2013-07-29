#! /usr/bin/python2 
# -*- encoding: utf-8 -*-
# 유닉스의 경우에,  cgi 스크립트를 실행하기 위해서는 현재 파일을 chmod +x 로 실행가능비트로 지정하고 #! /usr/bin/python2와 같이 경로를 지정한다. 
# windows에서는 이런게 필요없다.
# python 2.4.3
import urllib2
import re

html_content = urllib2.urlopen('http://www.dreamline.kr/dreamline-blog/').read()

matches = re.findall('드림라인', html_content);

if len(matches) == 0: 
   print 'I did not find anything'
else:
   print 'My string is in the html'
   print '\n 드림라인 \n'
