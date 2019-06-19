'''--------------------------------------------------------------
----------------------- SingleTon -------------------------------
--------------------------------------------------------------'''

class SingletonClass:
    init = None
    
    def __new__(cls):   #cls = ClassMethod
        if cls.init is None:
            cls.init = object.__new__(cls)
        return cls.init
    
    def aa(self):
        print('임의의 메소드')
    
    
class Sub(SingletonClass):
    pass

s1 = Sub()
s2 = Sub()
print(id(s1), ' ', id(s2)) 

s1.aa()
s2.aa()

print('\n사용 가능한 멤버 고정하기.')


class Animanl:
    __slots__ = ['name', 'age']
    
    def printData(self):
        print(self.name, ' ', self.age)

m = Animanl()
m.name = '호랭이'
m.age = 3
# m.eat='동물'
m.printData()

