import urllib.request
from bs4 import BeautifulSoup
from konlpy.tag import *
from urllib import parse #Encoding 해주기 위해서 사용.


# kkma = kkma()
kkma = Okt()
twitter = Twitter()
# hana = Hannanum()

sdata = parse.quote("이순신") #Encoding 작업.

url='https://ko.wikipedia.org/wiki/' + sdata
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page.read(), "lxml")
# print(soup)

wordlist =[]
#mw-content-text > div > p:nth-child(5)

for item in soup.select("#mw-content-text > div > p"):
    if item.string != None:
#         print(item.string)
        ss = item.string
        wordlist += twitter.nouns(ss)

print(wordlist)
print("단어 수: " + str(len(wordlist)))

print()
word_dict = {}
for i in wordlist:
    if i in word_dict:
        word_dict[i] += 1
    else:
        word_dict[i] = 1

print(word_dict)

#중복 단어 배제
setdata = set(wordlist)
print(setdata)
print('발견된 명사 수 (중복 제거):'+str(len(setdata)))

#csv 파일로 저장
import csv
import pandas as pd

try:
    f = csv.writer(open('lee1.csv', 'w' , encoding='euc-kr'))
    f.writerow(word_dict)
    
    
    f = csv.writer(open('lee2.csv', 'w' , encoding='euc-kr'))
    f.writerow(wordlist)
    
except Exception as e:
    print('err :', e)



# 차트 그리기.
from pandas import Series, DataFrame

li_data = Series(wordlist)
print(li_data)
print(li_data.value_counts()[:5])

seri_data = Series(word_dict)
print(seri_data)
print(seri_data.value_counts()[:5])

df = DataFrame(wordlist)
print(type(df))

import matplotlib.pyplot as plt
plt.rc('font', family='malgun gothic') # 한글이 깨졌을때 대처법.
plt.plot(seri_data.value_counts()[:5])
plt.xlabel('횟수 종류')
plt.ylabel('종류병 발생 수')
plt.title('단어 건수')
plt.legend('횟수')

plt.show()  #plot이 보이는 명령어.


















