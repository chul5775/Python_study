import urllib.request
from konlpy.tag import Okt

'''
twitter = Okt()
# wordlist = twitter.nouns("멋진 봄은 엄청 무더운 여름과 한들한들 시원한 바람이 부는 가을의 중간 계절이다")
# wordlist = twitter.morphs("멋진 봄은 엄청 무더운 여름과 한들한들 시원한 바람이 부는 가을의 중간 계절이다")
wordlist = twitter.pos("멋진 봄은 엄청 무더운 여름과 한들한들 시원한 바람이 부는 가을의 중간 계절이다")
print(wordlist)

# 명사구, 동사구, 형용사구로 묶어 주기
import nltk
parser_ko = nltk.RegexpParser("NP:{<Adjective>*<Noun>*}")
chunk_ko = parser_ko.parse(wordlist)
print(chunk_ko)
chunk_ko.draw()
'''
print('----------------------------------------------------')
f = open("abc.txt", "r", encoding='utf-8')
# print(f.read())

word_dic = {}
lines = f.read().split("\n")
print(lines)

twitter = Okt()

for line in lines:
    mallist = twitter.pos(line)
#     print(mallist)
    for word in mallist:
        if word[1] == "Noun":
            if not(word[0] in word_dic):
                word_dic[word[0]] = 0
            word_dic[word[0]] += 1 #단어 수 확인을 위한 dict
            
        
print(word_dic)

keys = sorted(word_dic.items(), key=None, reverse=True)
print(keys)

for word,count in keys[:20]:
    print("{0}{1}".format(word,count))
    
f.close()


print('word2vec을 활용하여 문장 분류 (의미를 선형으로 계산)-------------------------')
with open("abc.txt", "r", encoding='utf-8') as fr:
    results = []
    lines = fr.read().split("\n")
    
    for line in lines:
        mallist = twitter.pos(line, norm=True, stem = True)
        print('\n stem은 어근으로 출력하라. ex) 그래요 -> 그렇다.\n')
#         print(mallist)
        r = []
        for word in mallist:
            if not word[1] in ["Josa", "Punctuation", "Foreign", "Suffix", "Eomi"]:
                r.append(word[0])
            
        print(r)
        rl = (" ".join(r)).strip()
        results.append(rl)
        
        print(results)
        
data_file = 'news.txt'

with open(data_file, 'w', encoding='utf-8') as fw:
    fw.write('\n'.join(results))

from gensim.models import word2vec
# data = word2vec.LineSentence()

data = word2vec.LineSentence(data_file)
# print(data)
model = word2vec.Word2Vec(data, size=100, window =10, hs=1, min_count=2 ,sg=1) #CBOW, Skip-grammer
model.init_sims(replace=True) #필요없는 메모리는 unload
model.save("news.model")
print("ok")

model = word2vec.Word2Vec.load('news.model')

'''
1) 두 단어의 유사도 검사하기. = model.similarity
2) 가장 유사한 단어를 검색하기. = model_most_similar 
3) 긍정적인 단어 사이에 부정적인 단어가 끼어들었을때 높은 유사도 띄는애들. : positive=['단어','단어'], negative=['단어']
4) 이떄, 유사도는 유클리디언 거리 혹은 맨해튼 거리로 측정한다.
'''
print(model.similarity('원내대표','국회')) # 0.9932321
print(model.similarity('최고','호프')) # 0.9848665
print(model.most_similar('국회')) # [('하다', 0.9983276128768921), ('전날', 0.9980905652046204),,...]
print(model.most_similar(positive=['국회']))
print(model.most_similar(positive=['국회'], topn=5))
print(model.most_similar(positive=['국회','의원'], negative=['호프'], topn=5))





