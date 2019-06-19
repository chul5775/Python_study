'''--------------------------------------------------------------
---------- Class 내부에서 인스턴스 변수나 메소드를 호출할땐 self 사용 ------------
--------------------------------------------------------------'''

kor = 100 # 1. Module의 멤버

def abc():
    print('이거 함수')
    
class My:
    kor = 90 # 2. Class 멤버 변수(instance)
    
    def show(self):
        kor = 80 # 3. 지역변수
        print(kor) 
        print(self.kor)
        
        
m = My()
m.show()

'''------ <설명> ------
1. m.show를 해서 kor을 찾아가게 되면,
    self.kor 하게 되면 Class의 멤버 변수를 찾아가게된다.
    
2. 그리고 그냥 kor 하게 되면
    먼저, 지역변수 kor을 찾아보고
    
    그 이후 지역변수 kor이 없다면 Module의 kor을 찾아다님.
    마지막으로 아무곳에도 kor이 없다면 Err가 뜬다.
    
------ <결론> ------
1. 변수를 찾아가는 순서는
    지역변수 -> instance -> Module 순.
    
------------------ '''

class Our:
    a = 1
    
print(Our.a)

print()
our1 = Our()
print('our1.a : ', our1.a)

our2 = Our()
print('our2.a : ', our2.a)

our2.a = 7
print('our2.a : ', our2.a)

our2.kbs = 9
print('our2.kbs : ', our2.kbs)

