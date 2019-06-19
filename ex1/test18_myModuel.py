'''--------------------------------------------------------------
--------------------- 내가 만든 모듈 활용하기 ---------------------------
--------------------------------------------------------------'''

class Car:
    handle = 0
    speed = 0
    
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
        
    def showData(self):
        km = "킬로미터"
        msg = "속도:" + str(self.speed) + km
        return msg
    
print(Car.handle) # 원형 클래스의 멤버로 바로 출력.

'''------ <설명> ------
1. class Car:
   handle = 0 <-객체변수 (공유자원)
   speed = 0 <- 객체변수 (공유자원)
   
    def __init__(self, name, speed): <-name, speed는 지역변수
        self.name = name
        self.speed = speed
    
    def showData(self): <- km, msg 모두 지역변수
        km = "킬로미터"
        msg = "속도:" + str(self.speed) + km
        return msg
------------------ '''


print('-----------------')
car1 = Car('tom', 10) # Bound Method Call
print(car1.handle, ' ', car1.name, ' ', car1.speed)
car1.color = '검정'
print('car1.color : ', car1.color)

'''------ <설명> ------
1. 새로운 주소 만들어짐(car1)
    이 때,self는 car1이기 떄문에

2. name = 'tom'
    speed = '10' 의 변수안에 들어가진다.
    인스턴스이기 때문에 들어가지는거.
   
3. 이때 생성자를 타고 읽어들일때,
    __init__ 부터 읽는다. (자기 영역의 시작부분이기 때문에)

4. init부터 읽어들이기 때문에, name과 speed를 먼저 보고 생성자 안에 없으면
    공유 자원인 handle과 speed 영역으로 올라간다.

------------------ '''

print('------------------')
car2 = Car('james', 20)
print(car2.handle, ' ', car2.name, ' ', car2.speed)
# print('car2.color : ', car2.color) Err : color는 현재 car1에서만 만들어 주었기 때문에.
# print(Car.speed) 이것도 Err : 원형클래스에는 현재 Color가 없기때문에 Err임.

print(' 주소: ', Car, car1, car2)
print(' 주소: ', id(Car), id(car1), id(car2))


print('각 객체 멤버: ', car1.__dict__) # dict로 각 객체들의 멤버들을 읽어보기(결국에는 Dict형식으로 읽어들임.)
print('각 객체 멤버: ', car2.__dict__)


'''------ <결론 > ------
1. Car는 car1과 car2에게 생성자를 공유해 줬다.

2. 그러나, 세 가지 모두 
-------------------'''

print('\n 메소드 처리 ------------------')
print(car1.showData())  #Bound Method Call
print(Car.showData(car1))   #UnBound Method Call


'''---------------------- 2. 삼각형의 넓이를 계산하는 클래스 -----------------'''

class Tri:
    def __init__(self, b, h):
        self.b = b
        self.h = h
        
    def area(self):
        return self.b * self.h / 2
    
if __name__ == '__main__':
    t = Tri(3, 2)
    print(t.area())


'''==============================================================='''