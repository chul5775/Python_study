# XMlL 자료 처리
import xml.etree.ElementTree as et

### 방법1. 파일 읽기
xml_f = open("../testdata_utf8/my.xml", mode='r', encoding='utf-8').read()
print(xml_f)
print(type(xml_f))

## str을 ElementTree 객체로 변환
root = et.fromstring(xml_f)
print(type(root))
print(root.tag)
print(len(root))

### 방법2. ElementTree 객체로 직접 파싱
xmlfile = et.parse("../testdata_utf8/my.xml")
print(type(xmlfile))
# et.dump(xmlfile)

## root를 읽을 때 getroot하고 읽음
root = xmlfile.getroot() 
# root를 읽을 때 getroot하고 읽음
print(root.tag)
print()
print(root[0].tag)
print()
print(root[0][0].tag)
print(root[0][1].tag)

#속성값 얻어오기
print(root[0][0].attrib)
print(root[0][2].attrib)
print(root[0][2].attrib.keys())
print(root[0][2].attrib.values()) 
print(root[0][2].attrib.get("kor")) # 키를 주니까 값을 얻을 수 있다.

imsi = list(root[0][2].attrib.values())
print(imsi[0] + " " + imsi[1])

### ElenetTree는 Find를 사용 가능하다.
print('---------------------')
myname = root.find("item").find("name").text
mytel = root.find("item").find("tel").text
print(myname + " " + mytel)

print(' \n반복처리---------- ')
for child in root:
    print(child.tag)
    for child2 in child:
        print(child2.tag, child2.attrib)

print('특정 요소의 속성값 얻기----------')
for a in root.iter('exam'):
    print(a.attrib) #dic type의 속성값만 얻을 수 있다.
    
print()
children = root.findall('item')
for chi in children:
    re_id = chi.find('name').get('id')
    re_name = chi.find('name').text
    re_tel = chi.find('tel').text

    print(re_id, re_name, re_tel) 
    
    



















