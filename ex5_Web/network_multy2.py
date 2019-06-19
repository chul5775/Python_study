# 멀티 프로세싱 하고 웹자료 읽기

from multiprocessing import Pool
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
    
    pool = Pool(processes = 4) #4개의 프로세스 사용.(네트워크 상에서는 결국, 멀티 프로세스를 쓰는것이 젛음.)
    pool.map(get_cont, get_alinks()) 
    
    
    print("소요 시간: %s/sec"%(time.time() - start_time)) 
    
