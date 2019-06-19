# BeaurifulSoup으로 xml data 처리

from bs4 import BeautifulSoup

with open("../testdata_utf8/my.xml", mode = "r", encoding="utf-8") as f:
    xmlfile = f.read()
    
soup = BeautifulSoup(xmlfile, 'lxml')
print(soup.prettify())

itemTag = soup.findAll('item')
print(itemTag[0])

print()

nameTag = soup.findAll('name')
print(nameTag[0]['id'])

print()
for i in nameTag:
    nameTag = i.findAll('name')
    for j in nameTag:
        print(j['id'] + ' ' + j.string)

    telTag = i.findAll('tel')    
    for j in telTag:
        print('tel: ' + j.string)
    
    examTag = i.findAll('exam')    
    for j in examTag:
        print(j['kor'] + ' '+ j['eng'])