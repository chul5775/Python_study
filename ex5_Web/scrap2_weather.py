# 기상청 날씨 정보 SCraping
# http://www.kma.go.kr/XML/weather/sfc_web_map.xml

import urllib.request
import xml.etree.ElementTree as et
'''
순서  1) urlopen 해주기
순서 2) read로  2진 데이터로 읽기.
순서 3) decode로 언어 형식 맞춰주기
순서 4) 저장.
'''


try:
    webdata = urllib.request.urlopen("http://www.kma.go.kr/XML/weather/sfc_web_map.xml")
#     print(webdata)
    webxml = webdata.read()
    print(webxml) # 2진 데이타로 읽는다.
    
    webxml = webxml.strip().decode('utf-8')
    print(webxml) #decode로 풀어준다.
    webdata.close()
    
    with open('ftest.xml', mode = 'w', encoding='utf-8') as f:
        f.write(webxml)
        
except Exception as e:
    print('err: ', e)
    
print('읽기 성공')

xmlfile = et.parse('ftest.xml')
root = xmlfile.getroot()
print(root.tag)
print(root[0].tag)

print(root[0][0].attrib)
print(root[0][0].attrib.values())

children = root.findall("{current}weather")
print(children)

for i in children:
    y = i.get('year')
    m = i.get('month')
    d = i.get('day')
    h = i.get('hour')
    print(str(y) + '년' + str(m) + '월' + str(d) + '일' + str(h) + '시 현재')

datas=[]
for child in root:
#     print(child.tag)
    for i in child:
#         print(i.tag)
        local_name = i.text
        re_ta = (i.get('ta'))
        re_desc = (i.get('desc'))
        datas += [[local_name, re_ta, re_desc]]
        print(local_name + ", 온도:" + str(re_ta) + " " + re_desc)
        
print(len(datas))
print()
# 웹 이미지 읽기
# https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png
url = "https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png"
save_name = "test1.png"

# 다운로드 방법1.
urllib.request.urlretrieve(url, save_name) # 다운로드 후 바로 저장함.
print('다운로드 후 저장 성공')

# 다운로드 방법2. 
sava_name = "test2.png"
imsi = urllib.request.urlopen(url).read() #메모리(램)으로 올린 후 저장한다,

with open(save_name, mode='wb') as f:
    f.write(imsi)
    print('저장완료!')





    
    
    
    