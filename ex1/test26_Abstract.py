'''--------------------------------------------------------------
---------------------- 추상 클래스 (Abstract Class) ------------------
--------------------------------------------------------------'''
from abc import *


'''====================== 1. 부모클래스 용도로 작성 ======================'''

class AbstractClass(metaclass = ABCMeta): #추상 클래스
    
    @abstractmethod #추상 메소드를 위한 함수 장식자(deco)
    def abcMothod(self): # 추상 메소드
        pass
    
    def normalMethod(self):
        print('추상 클래스의 일반 메소드')
    
# pa = AbstractClass() TypeError: Can't instantiate abstract class AbstractClass with abstract methods abcMothod
# pa.normalMethod()

'''------ <설명> ------
1. 추상 클래스 사용을 위해서는 기본적으로 @abstarctmethod 함수 장식자를 써줘야 한다.

2. 추상 Class를 만들게 되면 더이상 객체를 만들 수가 없다.

3. 때문에, pa = AbstractClass()는 Err가 된다.
------------------ '''


'''====================== 2. 추상 메소드의 자식 Class1 만들기 ======================'''

class Child1(AbstractClass):
    name = " 난 차일드1"

    def abcMothod(self):
        print('추상 메소드를 재정의 ')

    
c1 = Child1() 
print(c1.name)
c1.abcMothod()

'''------ <설명> ------
1. 위와 같이  추상메소드를 사용해주기 위해서   @abstactmethod 함수 장식자로  꾸며준 함수를 다시 불러줘야한다.

2. java에서 interface에 만들고 그거 사용하려면 class에서 사용하듯이.

------------------ '''


'''====================== 2. 추상 메소드의 자식 Class2 만들기 ======================'''

class Child2(AbstractClass):
    name = " 난 차일드2"

    def abcMothod(self):
        print('추상 메소드를 override')
    
    def Hello(self):
        print('안녕')

    
c2 = Child2() 
c2.abcMothod()
c2.Hello()


poly = c1
poly.abcMothod()
poly = c2
poly.abcMothod()

