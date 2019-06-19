import urllib.request
import urllib.parse

print('<---방법 1--->')

url = "http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp"
data = urllib.request.urlopen(url).read()
# print(data)

text = data.decode('utf-8')
# print(text) # 이것으로 ElementTree 객체 또는 BeautifulSoup 객체화 할 수 있다.

print('<---방법 2) BueatifulSoup--->')
from bs4 import BeautifulSoup
data2 = urllib.request.urlopen(url)
soup = BeautifulSoup(data2, 'html.parser')
# print(soup)

print('타이틀')
title = soup.find('title').string
print(title)

wf = soup.find('wf')
print(wf) #하나만 잡아오기

wfs = soup.find_all('wf')
print(wfs) # 통쨰로 잡아오기.

print()
import urllib.request as req
url = 'https://news.v.daum.net/v/20190520114654131'
daum = req.urlopen(url)
soup = BeautifulSoup(daum,'lxml')
# print(soup)

print(soup.select_one('div#kakaoIndex a'))
print(soup.select('div#kakaoIndex a'))

print() #mw-content-text > div > p:nth-child(5)
url = 'https://ko.wikipedia.org/wiki/%EC%9D%B4%EC%88%9C%EC%8B%A0'
wiki = req.urlopen(url)
soup = BeautifulSoup(wiki, 'lxml')

print(soup.select('#mw-content-text > div > p'))
























