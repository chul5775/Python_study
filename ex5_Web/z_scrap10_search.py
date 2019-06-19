import requests
from bs4 import BeautifulSoup
import webbrowser

# 구글링 결과를 브라우저에 각각 출력하기.

def goProcess():
    base_url = "https://www.google.co.kr/search?q={0}"
    
    source_code = base_url.format("파이썬")
    plain_text = requests.get(source_code)
#     print(plain_text.text) # 응답 자료를 출력.
    
    parse_data = BeautifulSoup(plain_text.text, 'lxml')
#     print(parse_data)
#     link_data = parse_data.select('a')
    link_data = parse_data.select('.r a')
#     print(len(link_data))
    
    for link in link_data[:3]:
        url = link.get('href')
        print(url)
        url = "http://google.com" + url 
        webbrowser.open(url)#결과를 브라우저로 보여주는 기능이 있음!
    
goProcess()
    