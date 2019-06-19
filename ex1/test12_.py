'''--------------------------------------------------------------
--------------------------  일급 함수  ------------------------------
-----------------------------------------------------------------
<개요>
        - 함수 안에 함수 선언 가능
        
        - 인자로 함수 전달
        
        - 반환값이 함수인 경우
==============================================================='''

'''-------------------------------------------------------------'''
'''---------------------- 1. 함수  기본.  --------------------------'''
'''-------------------------------------------------------------'''
print('--<실습1: 함수 기본>--')
def func1(a, b):
    return a + b 

func2 = func1
print(func1(3, 4))
print(func2(3, 4))


'''-------------------------------------------------------------'''
'''---------------------- 2. 일급 함수.  --------------------------'''
'''-------------------------------------------------------------'''
print('--<실습2: 일급함수 >--')
def func3(func):
    
    def func4():
        print('나는 내부함수~~~')
        
    func4()
    return func

mbc = func3(func1)
print(mbc)
'''------ <설명> ------
1. func4는 func3의 내부함수이다.(함수안에 함수 선언)

2. func3의 반환값은 func이다. (반환값이 함수)

3. func3에 실습1에서 사용한 func1을 반환하였다. (인자로 함수 전달)
------------------ '''

'''-------------------------------------------------------------'''
'''---------------------- 3. 축약함수(Lamda)  ---------------------'''
'''---------------------  이름이 없는 한줄 짜리 함수  --------------------'''
'''-------------------------------------------------------------'''
print('--<실습3: 함수내의 덧셈 >--')
def Hap(x, y):
    return x + y 

print(Hap(1, 2))

print('--<실습4: 위의 함수를 Lamda로 압축>--')
print((lambda x,y : x + y)(1, 2))

g = lambda x,y : x*y 
print(g(3, 4))

print('--<실습5: Lamda 요약>--')
kbs = lambda a,su=10 : a+su
print(kbs(5))
print(kbs(5, 6))

print('--<실습6: 람다를 이용한 객체, 튜플, 딕셔너리 만들기.>--')
sbs = lambda a, *tu, **di : print(a, tu, di)
sbs(1,2,3,4,5,m=6, n=7)

print('--<실습7: Lamda의 List화>--')
li = [lambda a,b : a+b, lambda a,b : a*b]
print(li[0](3,4))
print(li[1](3,4))

print('--<실습8: 조건이 있는 Lamda >--')
print(list(filter(lambda a: a < 5, range(10))))
print(list(filter(lambda a: a % 2, range(10))))

'''==============================================================='''