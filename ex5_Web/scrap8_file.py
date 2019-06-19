# 스크래핑 자료 파일 저장
from bs4 import BeautifulSoup
import urllib.request as req
import datetime

url = "https://finance.naver.com/marketindex/"

res = req.urlopen(url)
soup = BeautifulSoup(res, "html.parser")

price = soup.select_one("span.value").string
print('uds : ', price)

t = datetime.date.today()
print(t)
fname = t.strftime("%y-%m-%d") + ".txt"

print(fname)
with open(fname, 'w', encoding='utf-8') as f:
    f.write(price)
    








