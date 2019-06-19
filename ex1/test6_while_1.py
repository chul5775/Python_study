'''------------- 1) 반복문 while 첫번째 --------------'''
'''------------- 1-1) while문 기본 -------------'''
print('\n실습1')
a = 1

while a <= 3:
    
    b = 1
    
    while b <= 4:
        print('a:'+ str(a) + ', b:' +str(b))
        b = b + 1
        
    a += 1


'''------------- 1-2) while을 이용해  순서가 있는 집합형 자료[LIST]의 길이만큼 자료를 출력 -------------'''
print('\n실습2')
colors = ['red', 'green', 'blue']
a = 0

while a < len(colors):
    print(colors[a], end = ' ')
    a += 1
    
print()
print(colors, len(colors))


'''------------- 1-3) 자료가 있으면 있는 만큼 뽑아서 사용하는 while문  -------------'''
print('\n실습3')

while colors:
    print(colors.pop()) # 하나씩 colors에서 뽑아냄.( pop 추출 )
print(colors, len(colors))


'''------------- 1-4) if문, while문, thread의 시간함수를 이용해서 프로그램을 끄기-------------'''
print('\n실습4')
import time
print(time.gmtime())
sw = input('폭탄 스위치를 누를까요?[y/n]')

if sw =='Y' or sw == 'y':
    count = 5
    
    while 1 <= count:
        print('%d초 남았어요.'%count) #여기서 %는 맵핑
        time.sleep(1) # 1초동안 잠을 잔다.
        count -= 1
    
    print('*!폭발!*')
   
elif sw == 'N' or sw=='n':
    print('작업 취소')
else:
    print('y또는 n을 누르시오')


'''==============================================================='''


