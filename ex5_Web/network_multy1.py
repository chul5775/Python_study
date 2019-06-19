# 멀티 프로세싱 없이 웹자료 읽기

import requests 
from bs4 import BeautifulSoup
import time

def get_alinks():
    req_data = requests.get("https://beomi.github.io/beomi.github.io_old/")
    html = req_data.text
#     print(html)
    soup = BeautifulSoup(html, 'html.parser')    
    a_titles = soup.select('h3 > a')
    
    data = []
    
    for t in a_titles:
       data.append(t.get('href'))
    
    return data    

def get_cont(link):
    a_link = 'https://beomi.github.io' + link
    req = requests.get(a_link)
    html = req.text
    soup = BeautifulSoup(html, 'lxml')
    print(soup.select('h1')[0].text)


if __name__ == '__main__':
    start_time = time.time()
    
#     print(get_alinks())
    for link in get_alinks():
        get_cont(link)
    
    print("소요 시간: %s/sec"%(time.time() - start_time)) # 소요시간 : 7.123546600341797/sec
    
    
    
