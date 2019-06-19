import urllib.request as req
from bs4 import BeautifulSoup

url = 'http://www.jc-direct.co.kr/'
car = req.urlopen(url)
soup = BeautifulSoup(car, 'html.parser')

#M_recom_wrap10 > ul.cont
carName = soup.select('#M_recom_wrap11 > ul.cont > li > p > a')
carPay = soup.select('#M_recom_wrap11 > ul.cont > li > span ')

carNames = []
carPays = []

for i in carName:
    carNames += {i.string}
        
for j in carPay:
    carPays += {j.string}

carInfo = dict(zip(carNames, carPays))

for key in carInfo.keys():
    print(key, ":", carInfo[key])