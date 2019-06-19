'''--------------------------------------------------------------
-------------------------- 클래스 ------------------------------
-----------------------------------------------------------------
<개요>
        1. OOP를 지원 (Object Oriented Prototype)
            1-1) 상속, 포함, 다형성을 구사 가능함.
        
        2. 이떄 생성자는 하나만 만들 수 있다.
==============================================================='''

'''--------------------- 1. 클래스와 함수 -------------------------'''

a = 10
print(a)

def func():
    print('함수라네')
    
class TestClass:
    aa = 1  #멤버 변수(전역)
    
    def __init__(self):
        print('생성자')
    
    def __del__(self):
        print('소멸자')
        
    def myMethod(self):
        name = 'tom' # 지역변수
        print(name)
        print(self.aa)
        
    def abc(self):
        self.myMethod()

'''------ <설명> ------
1. 생성자 오버로딩이 없다.

2. 그러나, 오버라이딩은 있다.

3. 여기서 사용된 self는 자바의 this와 비슷하다.

4. 소멸자(__del__)는 자동 호출 된다.(작업이 끝나면 자동으로 끝내주는 역할을 한다.) 
------------------ '''
        
        
'''--------------------- 2. 생성자 호출 -------------------------'''

print('<---생성자 호출 --->')
test = TestClass() # 생성자 호출, 객체(instance) 생성.
print(test.aa)
test.myMethod() # 생성자 이름으로 메소드 부르기(Bound Method Call).

print('<--원형 클래스 멤버 호출-->')
print(TestClass.aa) # 원형클래스 멤버 호출
# TestClass.myMethod() # 원형클래스이름으로 메소드 부르기(Error)
TestClass.myMethod(test) # (UnBound Method Call)

'''------ <설명> ------
1. Bound Method Call은  객체변 자동으로 타고가지만
  1-1) UnBound Method Call은 

------------------ '''

'''------ <깊은 설명> ------
1. class TestClass이 생성되면서
    
    =============================
    aa = 1
 
    def myMethod(self):
        name = 'tom' # 지역변수
        print(name)
        print(self.aa)
        
    def abc(self):
        self.myMethod()
    =============================
    
    을 가지면서, 자동으로 메모리를 확보한다.

2. test = TestClass()를 써주는 순간 새로운 객체가 생성되는데
   test2 = TestClass()를 써주면 또 다른 객체가 
   test3 = TestClass()를 써주면 또 또 다른 객체가
    이런식으로 TestClass Method를 가진 객체를 n개 만들 수 있다.
    이떄, 변수들은 서로다른 주소를 갖는다.
    
3. test = TestClass()
    
    =============================
    test.aa

    =============================

------------------ '''


'''--------------------- 3. Class의 Type과 주소 확인하기 -------------------------'''

print('<--- Type 확인 --->')
print(type(1))
print(type(1.5))
print(type(test)) # 얘는 Test Class Type이 된다/

print('<--- 주소 확인 --->')
print(id(TestClass))
print(id(test))


'''==============================================================='''
