'''--------------------------------------------------------------
------------------------- Main_Module ---------------------------
--------------------------------------------------------------'''
from ex1.test20_handle import PohamHandle

print('자동차 만세...')

class PohamCar:
    turnShow = '정지'
    
    def __init__(self, ownerName):
        self.ownerName = ownerName
        self.handle = PohamHandle() # 내용이 없는 생성자
    
    def TurnHandle(self,q):
        if q > 0:
            self.turnShow = self.handle.rightTurn(q)
        elif q < 0:
            self.turnShow = self.handle.leftTurn(q)
        elif q == 0:
            self.turnShow = "직진"
    

if __name__ == '__main__':
    print('<-- tom -->')
    tom = PohamCar('tom')
    tom.TurnHandle(20)
    print(tom.ownerName + '의 회전량은 ' + tom.turnShow + str(tom.handle.quantity))
    
    tom.TurnHandle(-30)
    print(tom.ownerName + '의 회전량은 ' + tom.turnShow + str(tom.handle.quantity))
    
    print('<-- Oscar -->')
    oscar = PohamCar('oscar')
    oscar.TurnHandle(0)
    print(oscar.ownerName + '의 회전량은 ' + oscar.turnShow + str(oscar.handle.quantity))
   