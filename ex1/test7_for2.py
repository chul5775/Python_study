'''-------------------------------------------------
----------------- (1) 반복문  for <두번쨰> --------------
================================================='''

'''-------------- (1-1) List를 이용한 for문 ----------'''
print('\n--<실습1>--')

temp = [1,2,3]
for i in temp:
    print(i, end = ' ')

print()
print([i for i in temp]) # List
#print((i for i in temp)) # Tuple
print({i for i in temp}) #set


'''-------- (1-2) for 다음에 나오는 변수를  for 왼쪽에서 이렇게 사용할 수 있다 --------'''

print('\n--<실습2>--')
temp2 = [i + 10 for i in temp]
print(temp2)

'''-------- (1-3) List를  내의 자료를 처리 후에 --------'''

print('\n--<실습3>--')

datas = [1, 2, 'a', True, 3]
li = [i * i 
      for i in datas 
      if type(i) == int]
print('직렬화 전:', li)

datas = {1,1,2,2,3}
li = [i * i for i in datas if type(i) == int]
print('직렬화 후:', li)

'''----------- (1-4) for를 활용한 dict ------------'''

print('\n--<실습4>--')

id_name = {1:'tom', 2:'james'}
name_id = {key:val for key, val in id_name.items()}
print('정상적인 출력:',name_id,)

name_id = {val:key for key, val in id_name.items()}
print('<응용> Key, Value를 뒤집어서 출력:',name_id)

'''--------- (1-5) for문장을 활용한 과일값 계산  ----------'''

print('\n--<실습5>--')

price = {'사과':5000, '배':3000, '수박':15000}
customer = {'사과':5, '배':3}

# bill = sum([1,2,3])
bill = sum(price[f] * customer[f] for f in customer)
print('손님이 구매한 과일값은 {}원'.format(bill))
'''와 대박 {}만써줘도 print문에서 받아들여'''

'''----------- (1-6) for문을 활욯한 수열 --------------'''

print('\n--<실습6>--')
print(list(range(1, 6)))
print(tuple(range(1, 6)))
print(set(range(1, 6)))
print(list(range(1,6,2)))
print(list(range(-10, -100, -20)))

'''
<설명>
print(list(range(-10, -100, -20)))의 경우엔
-10 => -100 으로 줄어드는데.
-20씩 줄어들었다.
즉, 초기식 , 조건 종료식, 증감식으로 보면 될거같다.
'''

'''---------- (1-7) for문에 range를 응용해서 구구단 출력  -------'''

print('\n--<실습7>--')

# for i in range(0,6):
for i in range(6):
    print(i, end = ' ')

print('\n--위 방법을 이용해 구구단 출력--')
# 2~9단 출력
for i in range(2, 10):
    for j in range(1,10):
        print('{} * {} = {}'.format(i,j, i*j), end = ' ')
    print() 

'''--------- (1-8) 1~100 사이의 3의 배수이면서 5의 배수의 합은? -------'''
print('\n--<실습8>--')
tot = 0

for i in range(1, 101):
    if i % 3 == 0 and i % 6 == 0:
        tot += i 

print('합은', tot)

'''--------- (1-9) 주사위를 던져 숫자합이 4의 배수인 경우 출력 (6,6) ------'''
print('\n--<실습9>--')

for i in range(6):
    n1 = i + 1
    
    for j in range(6):
        n2 = j + 1
        n = n1 + n2
        
        if n % 4 == 0:
            print(n1, n2)


'''------------- 1-10) n-gram --------------
<개요> n-gram 이란?
 - (문자열)에서 (n개)의 (연속된 요소)를 (추출)하기 
 
'''
print('\n--<실습10 n-gram>--')

ss= 'hello'

for i in range(len(ss) - 1):
    print(ss[i], ss[i + 1], sep= ' ')
    
'''==============================================================='''