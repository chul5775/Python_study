'''---------------- <개요> 정규표현식 ----------------------------

    1) 파이썬은 이 파일 자체가 모듈이다 .
    2) 정규표현식은 들어오는 데이터에 대해서 검색
'''    
    

import re
from re import _compile



ss = '1234 abc가나다ABCD_567_123_1kbs_nbc_air_a air air 하하'

'''---------------- 1) [RAW Mod 사용 ]----------------------------'''

print(re.findall(r'123', ss)) #RAW 모드 사용
#Raw모델은 이제 이 따옴표 안에있는 데이터는 escape가 아니고 검색을 위한 데이터야 라고해서 만들어진 모델이다.
print(re.findall(r'가나', ss))
print(re.findall(r'1', ss))
print(re.findall(r'[012]',ss))
print(re.findall(r'[0-9]',ss))
print(re.findall(r'\d',ss))
print(re.findall(r'[^0-9]',ss))
print(re.findall(r'\D',ss)) # 대문자는 숫자만 뺴고 find해줘라는 뜻
print(re.findall(r'[0-9].',ss)) # 점은 숫자 나오고 아무글자나 하나
print(re.findall(r'[0-9]?',ss)) # 낱낱히 한글자씪 모두 뽑는데 숫자만 뽑아줌.
print(re.findall(r'[0-9]+',ss)) # 플러스는 1이상 모든 숫자
print(re.findall(r'[0-9]*',ss)) #
print(re.findall(r'[0-9]{2}',ss)) # 이것도 낱낱히 나오는데, 숫자를 두개씩 찾아줌. 
print(re.findall(r'[0-9]{3}',ss)) # 이건 세개
print(re.findall(r'[0-9]{2,4}',ss)) # 2~4자리수 사이의 숫자만 찾아줌
print(re.findall(r'.bc',ss)) #
print(re.findall(r'1+',ss)) #
print(re.findall(r'^1+',ss)) #
print(re.findall(r'[^1]',ss)) #
print(re.findall(r'air',ss)) #
print(re.findall(r'air$',ss)) #
print(re.findall(r'[a-zA-Z가-힣]\w[^0-9]*',ss)) #
    
'''-------------- 1-1) <실습> tom, jame, oscar --------------'''
    
ss2 = 'tom80, james 100, oscar 50'
print(re.findall(r'\d',ss2))
print(re.findall(r'\d{2}',ss2))
print(re.findall(r'\d\d\d',ss2))
print(re.findall(r'\d{1,3}',ss2)) 
print()    

'''-------------- 1-2) <설명> flag 사용 --------------'''

ss3 = """My name is tom
I am happy"""
pattern = r'^.+'

print(ss3)
p = re.compile(pattern, re.MULTILINE)
print(p.findall(ss3))

'''
MULTILINE은 오류가 아닌데, eclipse가 못알아 들음.
출력해보면 잘 나와있당 
'''

'''==============================================================='''

