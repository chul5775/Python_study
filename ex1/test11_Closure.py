'''--------------------------------------------------------------
----------------------  클로저(Closure)  --------------------------
-----------------------------------------------------------------
<개요>
        - Scoper에 제약을 받지 않는 변수를 포함한 코드 블럭이다.
        
        - 내부 함수의 주소를 
        
==============================================================='''

'''---------------------- 1. 함수 지향적 언어의 재설명.  --------------------------'''
print('<--- 1. 함수 지향적 언어의 재설명 --->')
def MyTimes(a, b):
    c = a * b 
    #print(c)
    return c, a, b
'''------ <설명> ------
1. 파이썬은 이런식으로 return을 복수개 받을 수 있다.

2. 이때, return은 Tuple Type으로 받는다.
------------------ '''
    
print(MyTimes(2, 3))

kbs = MyTimes
print(kbs(2, 3))
print(id(kbs), id(MyTimes))
'''------ <설명> ------
1. a의 주소와 b의 주소를 치환하고 있다.

2. 즉 함수도 인스턴스의 주소를 가지고 있다.
------------------ '''

del MyTimes 
# print(MyTimes(2, 3))
print(kbs(2, 3))
'''------ <설명> ------
1. del을 쓰면 함수명을 지울 수 있다.

2. 하지만 주소를 넘겨받은 kbs는 현재 살아있는 상태이다.
------------------ '''

sbs = kbs(2,3)
print(sbs)

mbc = kbs
print(mbc(4,5))
'''------ <설명> ------
1. 즉, 함수의 주소는 객체의 주소이다.
------------------ '''

'''----------------------  2. 클로저(Closure)  --------------------------'''
print('\n<--- 2. closure --->')
def Outer():
    count = 0 #초기화

    def Inner():
        nonlocal count
        count += 1
        return count
    print(Inner())
    
Outer()
# print(count)
'''------ <설명> ------
1. 순서  Outer -> count = 0 -> Inner -> 지역변수 count

2. 하지만 이 상태로는 함수 내부함수를 참조할 수 없다.
------------------ '''

def Outer2():
    count = 0 #초기화

    def Inner2():
        nonlocal count
        count += 1
        return count
    return Inner2 
'''------ <설명> ------
1. Closure의 내부 함수를 return 해준다.

2. 그리고 이렇게 Inner를 넘겨주는게 Closure이다.
------------------ '''

aaa = Outer2()
print(aaa())
print(aaa())
print(aaa())

bbb = Outer2()
print(bbb())
print(bbb())

'''----------------------  3. 수량 / 단가 예제  --------------------------'''
print('<--- 3. 수량 / 단가  --->')
def Outer3(tax):
    def Inner3(su, dan):
        amount = su * dan * tax
        return amount
    return Inner3

jan = Outer3(0.1)
retult = jan(5, 50000)
print(retult)

retult2 = jan(3, 120000)
print(retult)

may = Outer3(0.15)
result2 = may(5, 12000)
print(result2)


'''==============================================================='''