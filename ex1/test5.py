'''------------- 1) 조건 판단문 -------------- 

1) Python은 들여쓰기가  block처리 이므로, block에 주의해야한다.
     때문에, 들여쓰기로 조건문에 대한 참 or 거짓에 대한 결과를 넣어주면 된다.

2) 조건 판단문 안에는 
'''
'''------------- 1-1) if문  -------------''' 
print('\n<실습1>')
var = 5

if var >= 3:
    print('크구나')    
    if var > 4:
        print('블락 안의 블락') 

else:
    print('작아요')

print('\n<실습2>')

# else if 문

jumsu = 90
if jumsu >= 90:
    print("우수")
elif jumsu >= 70:
    print("보통")
else:
    print("저조")
    
print('\n<실습3>')


'''------------- 1-2) 키보드 입력을 통한 if문과 형변환 -------------

1) 키보드로 입력받는 값은 String Data이다.
때문에, 정수 처리를 해주려면  형변환을 사용해 주어야 한다. (int(), str())
'''

jumsu = int(input('점수 입력:')) # 형변환 int(), str()

if jumsu >= 90:
    print("input 우수")
elif jumsu >= 70:
    print("input 보통")
else:
    print("input 저조")

if 90 <= jumsu <= 100:
    print("input 우수2")
elif jumsu <= 70:
    print("input 보통2")
else:
    print("input 저조2")

print('\n<실습4>')


'''------------ 1-3) List를 통한 if문 사용 -------------''' 
names = ['홍길동', '신기해', '공기밥']
if 'go길동' in names:
    print('친구야')
else:
    print('누구야')
    
print('\n<실습5>')


'''------------- 1-4) if문 직렬화 -------------''' 
a = 'kbs'
b = 9 if a =='kbs' else 11
print(b)

a = 11
b = 'mbc' if a==9 else 'kbs'
print(b)


'''------------- 1-4-1) if문 직렬화 예제  와  튜플, 리스트를 if문 처럼 사용하기. -------------''' 
print('\n<실습6>')
a = 1
if a > 5:
    result = a*2
else:
    result = a+2
print('변하기 전 result값:',result)

'''
 ↓ 위의 if문은 한줄짜리로 이렇게 변했음.
'''
result = a * 2 if a > 5 else a + 2
print('변하기 후 result값:',result)
print()

print('튜플 결과 반환:',(a + 2, a * 2)[a > 5])

'''
<설명>
    (a + 2, a * 2) 
(튜플의 0번째, 튜플의 1번쨰 )

    [a > 5]
[List의 0번째]

<설명 2>
여기서 List의 조건을 만족(참)할 때 , 튜플의  1번째 (오른쪽 값)를 출력하고
조건을 만족하지 않을때(거짓), 튜플의 0번쨰 (왼쪽 값)를 출력한다.
'''    
    
'''==============================================================='''



