# python 2.6
# http://toors.tistory.com/entry/Python-BeautifulSoup%EC%9C%BC%EB%A1%9C-%EA%B2%8C%EC%8B%9C%ED%8C%90-%EA%B8%81%EC%96%B4%EC%98%A4%EA%B8%B0-%ED%8C%A8%ED%84%B4
# string usaged

import urllib
import BeautifulSoup

html = '<div><span><a href=http://naver.com>naver.com</a></span></div>'
soup = BeautifulSoup.BeautifulSoup(html)

print soup.prettify()
