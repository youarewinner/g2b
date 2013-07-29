# -*- coding: utf-8 -*-  test
# python 3.2
import urllib.request
import re

html_content = urllib.request.urlopen('http://www.kict.re.kr/')
print(html_content.read())

matches = re.findall('Home', html_content);

if len(matches) == 0: 
   print ('I did not find anything')
else:
   print ('My string is in the html')
