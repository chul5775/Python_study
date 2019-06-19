from bs4 import BeautifulSoup

print('방법 1-------------')

import urllib.request

url = "https://movie.naver.com/movie/sdb/rank/rmovie.nhn"
data = urllib.request.urlopen(url).read()
soup = BeautifulSoup(data, 'html.parser')
# print(soup)
# print(soup.select('div.tit3'))
# print(soup.select('div[class=tit3]'))
for tag in soup.select('div[class=tit3]'):
    print(tag.text.strip())


print('방법2 --------------')

import requests

data = requests.get(url).text
soup = BeautifulSoup(data, 'html.parser')
# print(soup)
m_list = soup.findAll("div","tit3")
# print(m_list)
title = 'abcdefg'
# print(title[title.find('b'):title.find('f')]) # 범위 지정해서 읽어오기.

for i in m_list:
#   print(i) <a href="/movie/bi/mi/basic.nhn?code=171539" title="그린 북">그린 북</a>
    title  =i.findAll('a')
    print(str(title)[str(title).find('title="') + 7:str(title).find('">')])

print('\n--------------------------------------------')

count = 1

for i in m_list:
    title = i.find('a')
    print("[", count , "위] " + title.string)
    count += 1
    
    
    
    
    
    