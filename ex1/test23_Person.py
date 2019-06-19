'''--------------------------------------------------------------
----------------------------- 상속 관계  (2) ------------------------
--------------------------------------------------------------'''
from builtins import staticmethod, classmethod
print('이러저러 하다가')

'''------------ 1. 부모클래스 용도로 작성, 다른 모듈에 작성했다 가정 -----------'''
# say = "모듈 수준의 전역 변수" 

class Person:
    say = '난 사람이야~~~'
    nai = 20 #(8) Employee Class로 부터 올라옴.(nai)를 만남. 이제 다시 밑으로 끌고 내려감.
    __kor = 90 # private Method
    
    def __init__(self, nai): 
        print('Person 생성자') 
        self.nai = nai
        
    def PrintInfo(self):
        print('나이:{}, 이야기:{}'.format(self.nai, self.say))
        
    def Hello(self):
        print('안녕')
        

    
    @staticmethod
    def sbs(tel):
        print('sbs-staticmethod: ', tel)
    
    @classmethod
    def kbs(cls):
        print('kbs-classmethod: ', cls.say, cls.nai)
        
print('\n<-#-#-#- 부모 클래스  -#-#-#->')
print(Person.say, Person.nai) #UnBound
# Person.Hello() TypeError: Hello() missing 1 required positional argument: 'self

p = Person('22')
p.Hello()



'''------------ 2. Person의 자식클래스 Employee-----------'''


print('\n<-#-#-#- Person의 자식 Class (1) Employee -#-#-#->')

class Employee(Person): # (7) nai를 찾으러 부모 Class(Person)로 가봄.
    say = "일하는 동물" # (4) say와 매칭 확인되는 class 객체 변수를 찾아감. 
    subject = "근로자" # (5) nai와 매칭되는 class 객체변수를 찾아갔지만 없음.
                        #(6) nai는 건너 뛰고 subject와 매칭되는 객체변수를 찾아감.
    
    def __init__(self): # (3) 가장먼저 생성자인 여기로 옴. 
        print('Employee 생성자')
        
    def PrintInfo(self):    #Override
        print('Employee 메소드 중 하나')

    def EprintInfo(self):
        say ='푸하하하' 
        print(say, super().say, self.say, self.subject, self.nai)
        self.PrintInfo()
        super().PrintInfo() #무조건 부모한테감.
        
'''------ <Person을 부모로 한 순간 이렇게 보면 됨.> ------
--------- 없으면 와서 쓰고 꼭 필요하면 super로 불러써 -------

   say = '난 사람이야~~~'
   nai = 20 #(8) Employee Class로 부터 올라옴.(nai)를 만남. 이제 다시 밑으로 끌고 내려감.   
    
   def __init__(self, nai): 
       print('Person 생성자') 
       self.nai = nai
        
   def PrintInfo(self):
       print('나이:{}, 이야기:{}'.format(self.nai, self.say))
        
   def Hello(self):
       print('안녕')
        
------------------ '''


em = Employee() # (1) Class를 객체 변수로 만들어줌.
print('\n---<자식 클래스 employee 생성자 실행>---')
print(em.say, em.nai, em.subject) # (2) 실행 (9) 출력

print('\n---<자식 클래스 employee의  PrintInfo실행>---')
em.PrintInfo() 

print('\n---<자식 클래스 employee EPrintInfo 함수 실행>---')
em.EprintInfo() 

print('\n---<자식 클래스 employee에서 부모클래스의  Hello함수 실행>---')
em.Hello()



'''------------ 3. Person의 자식클래스 Worker -----------'''

print('\n<-#-#-#- Person의 자식 Class (2) Worker -#-#-#->')

class Worker(Person):
    def __init__(self, nai):
        print('Worker 생성자')
        super().__init__(nai) #Bound Method Call (super로 한번 튕겨서 부모한테 갔기 때문에)
        
    def PrintInfo(self):    #Override
        print('Worker 메소드 중 하나')
    
    def WprintInfo(self):
        super().PrintInfo()

wo = Worker('25')

print('\n---<자식 클래스 Worker에서 PrintInfo 함수 실행>---')
wo.PrintInfo()

print('\n---<자식 클래스 Worker에서 WprintInfo 실행 후  부모 클래스의 PrintInfo 함수 실행>---')
wo.WprintInfo()



'''------------ 4. Person의 자식클래스 Worker의 자식인  Programmer-----------'''

print('\n<-#-#-#- Person의 자식 Class Worker의 자식 Class (2 - 1) Programmer -#-#-#->')

class Programmer(Worker):
    def __init__(self, nai):
        print('Programmer 생성자')
        Worker.__init__(self,nai)
        
    def WprintInfo(self):
        super().WprintInfo()
    
pr = Programmer('33')
print(pr.say, pr.nai)
pr.WprintInfo()

print('\n')

a = 10

print(type(a))

print(type(pr))

print(type(wo))

print(Person.__bases__)

print(Programmer.__bases__)

print(Worker.__bases__)


print('\n 함수 장식자(deco)의 static Method를 이용.')
pr.sbs('111-1111')
Person.sbs('222-2222')

print('\n 함수 장식자(deco)의 Class Method를 이용.')
pr.kbs()
Person.kbs()



'''============================================================'''
