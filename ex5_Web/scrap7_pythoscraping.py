# http://www.pythonscraping.com/pages/page3.html

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

def processFunc(url):
    try:
        html = urlopen(url)
        print(html)
        
    except Exception as e:
        return None

    try:
        bsObj = BeautifulSoup(html, 'html.parser')
        title = bsObj.body.h1
        
        print('연습1 자손과 자식태그----------------')
#         for child in bsObj.find("table", {"id":"giftList"}).chilren:
#         for child in bsObj.find("table", {"id","giftList"}).descendants:
#             print(child)
            
        print('연습2 형제 태그----------------')
#         for sibling in bsObj.find("table", {"id":"giftList"}).tr:
#         for sibling in bsObj.find("table", {"id":"giftList"}).tr.next_siblings:
#             print(sibling)
        
        print('연습3 : 형제 태그 ---------')    
        print(bsObj.find("img",{"src":"../img/gifts/img1.jpg"}))\
        .parent.previous_sibling.get.text()
        
    except Exception as err:
        return None    

    return title
    
    
title = processFunc('http://www.pythonscraping.com/pages/page3.html')

if title == None:
    print('처리 실패')
else:
    print(title)
    
