'''----------- 1)집합 자료형 :String - 순서o, 수정 x -----------'''

s = "sequence"
print(len(s), s.count('e')) 

'''-------------------- 1-1) 슬라이싱 --------------------'''

print(s[0], s[2:4], s[:3], s[3:])

'''
<결과> s qu seq uence
<사용법> 대괄호 안에다가 Index를 적어주면 된다.
<설명> 글자수는 모두  다르지만 , 모두 1byte씩 가지고 있다.  
'''

print(s[-1], s[-4:-2])
print(s[::2]) 
'''
<결과> e en
      sqec
<설명> ::은 
'''
print(s[0:8:2])

'''----------------- 1-2)split(문자열 나누기) -----------------'''

ss = 'mbc'
print(ss, id(ss))
ss = 'abc'
print(ss, id(ss))

ss2 = "mbc kbs"
ss3 = ss2.split(sep=' ')
print('ss3 =',ss3, ss3[0], ss3[1])
'''
<결과> ss3 = ['mbc', 'kbs']
<설명> 하나의 문자였지만  slice로 인해 위에 보이는 것 처럼 로  서로 다른 주소를 갖는다.
'''

'''----------------- 1-3)join(문자열 더하기) -----------------'''

ss4 = ':'.join(ss3)
print(ss4)


'''--------------- 1-4)replace(문자열 바꾸기 ) ---------------'''

ss5 = "Life is too short"
ss6 = ss5.replace("Life", "Your leg")
print(ss6)

'''
<결과> Your leg is too short
'''

'''======================================================'''
