'''------------- 1) 반복문 while 두번째 --------------'''
'''------------- 1-1) While문에서 else 수행시키기(정상종료) -------------'''
print('\n<실습1>')
a = 0

while a < 10:
    a += 1
    print(a)
else:
    print('while 수행')
    
print('while 수행 후 %d'%a)


'''------------- 1-2) While문에서 else 수행시키기(비정상종료) -------------'''
print('\n<실습2>')
while a < 10:
    a += 1
    if a == 3: continue
    if a == 5: break
    print(a)
else:
    print('while 수행')
    
print('while 수행 후 %d'%a)


'''------------- 1-3) 홀 / 짝 출력   -------------'''
print('\n<실습3>')
while True:
    a = int(input('숫자 입력:'))
    if a == 0:
        print('프로그램 종료')
        break
    elif a % 2 == 0:
        print('%d는 짝수'%(a))
        continue
    elif a % 2 == 1:
        print('%d는 홀수'%(a))
        continue
     

'''------------------ 1-4) 임의의 숫자 맞추기 -------------------'''
print('\n<실습4>')
import random
# print(random.randint(1, 100)) random 예제
num = random.randint(1, 10)
while True:
    print("1~10 사이의 예측한 정수를 입력")
    guess = input()
    su = int(guess)
    
    if su == num:
        print('와우 성공' * 5)
        break
    elif su < num:
        print('더 큰 수를 생각하시오.')
    elif su > num:
        print('더 작은 수를 생각하시오.')
        
        
'''
num을 pc,
su를 사용자라고 생각해보면
대화형 처럼 사용가능.
'''

'''==============================================================='''
