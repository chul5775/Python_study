import requests
from bs4 import BeautifulSoup

def go():
    base_url = "http://www.naver.com/index.html"
   
    source_code = requests.get(base_url)
    
   
    plain_text = source_code.text
    
    
    convert_data = BeautifulSoup(plain_text, 'lxml')
    print(type(convert_data ))

#     for link in convert_data.findAll('a', {'class': 'h_notice'}):
    for link in convert_data.findAll('a'):
        href = base_url + link.get('href')  #Building a clickable url
        print(href)                          #displaying href


go()