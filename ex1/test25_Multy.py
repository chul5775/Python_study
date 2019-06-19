'''--------------------------------------------------------------
-------------------------------- 다중 상속 --------------------------
--------------------------------------------------------------'''

'''------------ 1. 부모클래스 용도로 작성 (Tiger, Lion) -----------'''
class Tiger:
    data = "호랑이 세상"
    
    def cry(self):
        print('호랑이 어흥')
    
    def eat(self):
        print(' 맹수는 고기를 엄청 좋아함')

class Lion:
    data = "라이언 세상"
    
    def cry(self):
        print('사자 으르렁')
    
    def hobby(self):
        print('백수의 왕은 낮잠을 즐겨함. 가끔 채팅도 즐김')

'''------------ 2. Tiger와 Lion을 부모 Class로 하는 자식 Class Liger를 생성 -----------'''
print('\n<--- 자식 class (1) Liger1 ---->\n')
class Liger1(Tiger, Lion):
    pass

ani1 = Liger1()
ani1.cry()
ani1.hobby()
print(ani1.data)

'''------ <설명> ------
1. 먼저 적어준 녀석에게 우선순위 있다.

2. 때문에, Tiger -> Lion
------------------ '''

print('\n<--- 자식 class (2) Liger2 ---->\n')

class Liger2(Lion, Tiger):
    data = "라이거 만세"
    
    def hobby(self):
        print('웹 프로그래밍 하기')
        
    def play(self):
        print('라이거 고유 메소드')
        self.hobby()
        super().hobby()
        print(self.data, ' ', super().data)
    
    pass

ani2 = Liger2()
ani2.cry()
ani2.hobby()
ani2.play()
print(ani2.data)


'''============================================================'''