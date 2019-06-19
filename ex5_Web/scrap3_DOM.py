# DOM 처리 방식과 유사한 방법제고 모듈
from xml.dom.minidom import parse

document = parse(open("ftest2.xml", encoding = 'utf-8'))
print(document.toxml())

names = document.getElementsByTagName('name')
print(names)
print(names.length)

print()
item = document.childNodes
print(item[0].localName)
print()
# name = item[0].childNodes
text = names[0].childNodes
print(text)