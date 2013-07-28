#! /usr/bin/python2 
# -*- encoding: utf-8 -*-
# 유닉스의 경우에,  cgi 스크립트를 실행하기 위해서는 현재 파일을 chmod +x 로 실행가능비트로 지정하고 #! /usr/bin/python2와 같이 경로를 지정한다. 
# windows에서는 이런게 필요없다.
# python 2.6
# Beautiful Soup (2.1.1)
# http://pydev.tistory.com/10
# 웹을 가지고 놀기 위해서는 먼저 웹의 언어인 HTML을 잘 구사할 수 있어야 한다.세상에는 프로그래머가 HTML을 잘 말하고 잘 알아듣기 위해 사용하는 HTML 파서가 무수히 많다.  
# 그중에서 사용하기 쉬운 파서를 하나 고르자면 Beautiful Soup을 들수 있다.  Beautiful Soup은 파이선으로 작성되었으며, 동적 스크립트언어의 장점을 잘 활용한다.
#
import urllib
from BeautifulSoup import BeautifulSoup

html_source = urllib.urlopen('http://www.naver.com').read()

#soup = BeautifulSoup(html_source) 
# 여기에 한글을 읽을 려면, "euc-kr" , "utf-8" 등
soup = BeautifulSoup(html_source, fromEncoding="euc-kr")

# 테그 이름을 변수 이름으로 사용할 수 있다.
print soup.html.head.title

# 계층구조의 중간단계를 생략할 수 있다.
print soup.title

# 테그 안에 다른 테그가 없는 경우 string 속성으로 테그 내용을 얻을 수 있다.
print soup.title.string

# 같은 이름의 테그가 여러개 있다면 제일 먼저 나오는 테그를 알려준다.

print soup.p

# dictionary 문법을 사용하여 테그의 속성만 얻을 수도 있다.
print soup.p['class']

# 없는 테그를 지칭하면 (BeautifulSoup.) Null 객체를 반환한다.
print soup.body.title

# soup('p') 은 첫번째 뿐아니라 모든 p 테그 목록을 반환한다.
#print soup('p')

# 두번째 아규먼트로 테그의 속성을 제한할 수도 있다.
print "# print soup('p')[0] 두번째 아규먼트로 테그의 속성을 제한할 수도 있다."
print soup('p')[0]


print "# print soup('p')[1] 세번째 아규먼트로 테그의 속성을 제한할 수도 있다."
print soup('p')[1]

print "# for 문 "
#for  x  in soup('p')[:] :
#	print soup('p')[x]
#	x = int(y)
	




print "# print soup('img', { 'name': 'main', })"
print soup('img', { 'name': 'main', })

print '-------------------------------'
print "#soup('p', 'tit')"
print soup('p', 'tit')

print '-----------------'
print "# print soup('p', { 'class': 'tit' })"
print soup('p', {'class': 'tit'})

print "# 결국 soup('p', 'tit') 와 soup('p', { 'class': 'tit' }) 과 같다. CSS 분류를 쉽게 지정할 수 있다."


print "# parent 속성은 계층구조상 한칸 위에 있는 테그를 지칭하고, 반대로 contents 속성은 계층구조상 한칸 아래에 있는 테그 목록을 반환한다. nextSibling 와 previousSibling 은 계층구조상 같은 위치에 있는 바로 앞뒤 테그를 지칭한다. "
print soup('p').parent

print "---------------"
print " nextSibling 와 previousSibling 은 계층구조상 같은 위치에 있는 바로 앞뒤 테그를 지칭한다. "
print soup('p')[0].nextSibling
print soup('p')[0].next

