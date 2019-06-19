'''--------------------------------------------------------------
---------------------------- TEST 추상 클래스 ------------------------
--------------------------------------------------------------'''
from abc import *

class Employee(metaclass = ABCMeta):
    irum = "이름"
    nai = "나이"
    
    @abstractmethod
    def Pay(self):
        if self.ilsu > 0:
            
            self.pay = self.ilsu * self.ildang
       
       
        elif self.sales > 0:
            
            self.pay = self.salary + (self.sales * self.commision)
        
    @abstractmethod
    def data_print(self):       
            print('이름:', self.irum, '나이:', self.nai)

        
    def irumnai_print(self):
        pass

class Temporary(Employee):
    ilsu = '일수'
    ildang  = '일당'
    
    def __init__(self, irum, nai, ilsu, ildang):
        self.irum = irum
        self.nai = nai
        
        self.ilsu = ilsu
        self.ildang = ildang
        
        self.Pay()
        
    def Pay(self):
        super().Pay()
        
    def data_print(self):
        super().data_print()
        print('월급:', self.pay)


class Regular(Employee):
    salary = '급여'
    
    def __init__(self, irum, nai, salary):
        self.irum = irum
        self.nai = nai
        
        self.salary = salary 

    def Pay(self):
        pass
    
    def data_print(self):
        super().data_print() 
        print('급여:', self.salary)


class Salesman(Regular):
    sales = '실적'
    commission = '수수료율(예:0.25)'
    
    def __init__(self, irum, nai, salary, sales, commission):
        self.irum = irum
        self.nai = nai
        self.salary = salary 
        
        self.sales = sales
        self.commission = commission
        
        self.pay()
    
    def Pay(self):
        super.Pay()
    
    def data_print(self):
        super().data_print() 
        print('실수령액:', self.pay)
        

t = Temporary("홍길동", 25, 20, 15000)
r = Regular("한국인", 27, 35000000)
s = Salesman("손오공", 29, 1200000, 500000, 0.25)

t.data_print()
r.data_print()


