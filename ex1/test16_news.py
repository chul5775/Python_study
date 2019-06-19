'''--------------------------------------------------------------
-------------------------- 신문 스크랩하기 ------------------------------
-----------------------------------------------------------------
<개요>
        1. 스크랩 순서
            1-1) 웹에서 기사 스크랩하기.
            1-2) 신문기사만 스크랩하는 newspaper를 import하기.
            1-3) download -> parse
            1-4) 필요에따라서 re.sub로 원하는대로 조건을 뽑아 읽어들이기.
==============================================================='''
from newspaper import Article
import re
from newspaper.api import languages

url = "http://star.mt.co.kr/stview.php?no=2019051408201390616&outlink=1&ref=https%3A%2F%2Fsearch.daum.net"
a = Article(url, languages='ko')
a.download()
a.parse()
print("제목 : ", a.title)

print('**' * 10)
ss =a.text
# print(ss)

print('<----  한글만 사용 가능하게 조건 걸기  ---->')
ss2 = re.sub(r'[^가-힣\s]', '', ss)
print(ss2)


'''==============================================================='''

