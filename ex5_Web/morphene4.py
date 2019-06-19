# Corpus (말뭉치) : 언어의 표본을 담아둔 묶은(사전)
from konlpy.corpus import kobill # 정치 관련 사전

# 파일 읽어오기 (1)
files_ko = kobill.fileids()
# print(files_ko) # 문서 확인하기.

# 파일 읽어오기 (2)
doc_ko = kobill.open(r'mynews.txt').read()
# print(doc_ko)
# 의미 단어 추출 (Tokenize)
from konlpy.tag import Okt

t = Okt()

tokens_ko = t.morphs(doc_ko) # 문서를 token으로 분리
print(tokens_ko) 

import nltk
ko = nltk.Text(tokens_ko, name='원내대표') # 그런 단어가 있는지 검색할때 쓰는 nltk.Text

print(ko)
print('토큰 정보 확인-----')
print(len(ko.tokens)) # 608개
print(len(set(ko.tokens))) #유니크한개 293개
fre_dist = ko.vocab()
print(fre_dist) # <FreqDist with 293 samples and 608 outcomes>

# from matplotlib import rc 
# rc('font', family='malgun gothic')
# ko.plot(50)

#워드 클라우드로 출력
print(ko.vocab())
print(type(ko.vocab()))
print(dir(ko.vocab()))

#dict_items로 출력
data = ko.vocab().items()
print(data)

import csv
with open('words.csv', 'w', encoding='utf-8')as f:
    f.write('word,freq\n') # header
    writer = csv.writer(f)
    writer.writerows(data)

