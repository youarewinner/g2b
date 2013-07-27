# python 2.6
# http://toors.tistory.com/entry/Python-BeautifulSoup%EC%9C%BC%EB%A1%9C-%EA%B2%8C%EC%8B%9C%ED%8C%90-%EA%B8%81%EC%96%B4%EC%98%A4%EA%B8%B0-%ED%8C%A8%ED%84%B4
##
import urllib
import BeautifulSoup

data = urllib.urlopen('http://comic.naver.com/webtoon/list.nhn?titleId=20853&weekday=fri')
soup = BeautifulSoup.BeautifulSoup(data)
cartoons = soup.findAll('td', attrs={'class':'title'})
title = cartoons[0].find('a').text
link = cartoons[0].find('a')['href']

print title, link
