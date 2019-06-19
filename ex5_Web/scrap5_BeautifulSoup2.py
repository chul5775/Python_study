from bs4 import BeautifulSoup

html_data = '''
<html>
<body>
<h1>제목 태그</h1>
<p>뷰티풀숍으로 읽기</p>
<p>원하는 자료 추출1</p>
<p>원하는 자료 추출2</p>
</body>
</html>
'''

# 지금은 그냥 string 타입임.
print(type(html_data))

# 뷰티풀 숖 타입으로 변환시켜주기
soup = BeautifulSoup(html_data, "html.parser")
print(type(soup))

print()
h1 = soup.html.body.h1
p1 = soup.html.body.p
p2 = p1.next_sibling.next_sibling
p3 = p1.next_sibling.next_sibling.next_sibling.next_sibling 


print('h1 : ', h1.string)
print('p1 : ', p1.string) #  최초의 p태그를 가지고 온다
print('p2 : ', p2.string) # next_sibling 사용법 (1)
print('p3 : ', p3.string) # next_sibling 사용법 (2)
print('\n find() 메소드 사용 --------------------')

html_data2 = """
<html>
<body>
<h1 id='title'>제목 태그</h1>
<p>뷰티풀숍으로 읽기</p>
<p attr="my">원하는 자료 추출</p>
</body>
</html>
"""

soup2 = BeautifulSoup(html_data2, "html.parser")
print("궁금")
print("title : " + soup2.find(id='title').string)
print("my : " + soup2.find(attr='my').string)



print('\n find_all() 메소드 사용 --------------------')

html_data3 = """
<html>
    <body>
        <h1 id='title'>제목 태그</h1>
        <p>뷰티풀숍으로 읽기</p>
        <p attr="my">원하는 자료 추출</p>
        
        <div>
            <a href='http://www.naver.com'>naver</a><br>
            <a href='http://www.daum.net'>daum</a><br>
        </div>
    </body>
</html>
"""

soup3 = BeautifulSoup(html_data3, "html.parser")
# print(soup3.prettify())
links = soup3.find_all('a')
print(links) #List Type으로 집어 넣엇다.

print('링크스')
for i in links:
    href = i.attrs['href']  #주소
    text = i.string     #요소
    print(href, ' ', text)


print('정규 표현식')

import re
links2 = soup3.find_all(href=re.compile(r'^http://'))
print(links2)

for i in links2:
    print(i.attrs['href'])

print()
print(soup3.find_all('p'))
print(soup3.find_all(['p', 'h1']))

aa = soup3.find_all(string=['제목태그','원하는 자료 추출'])
print(aa[0])
# print(aa[1])


print('\nCSS selector를 사용----------------')

html_data4 = """
<html>
    <body>
        <div id = 'hello'>
            <a href='http://www.naver.com'>naver</a><br>
            <ul class = 'world'>
                <li>안녕</li>
                <li>반가워</li>
            </ul>
        </div>
            <a href='http://www.daum.net'>daum</a><br>
        <div>good</div>
    </body>
</html>
"""

soup4 = BeautifulSoup(html_data4, 'lxml')
a = soup4.select_one("div#hello > a").string  #집합자료가 아님.
print('a:', a)


uls = soup4.select('div#hello > ul.world > li')
for i in uls:
    print('li : ', i.string)












