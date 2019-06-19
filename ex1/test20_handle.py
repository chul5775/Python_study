'''--------------------------------------------------------------
----------- 다른 클래스의 멤버로 사용할 부품 클래스 gandle 작성 -----------------
--------------------------------------------------------------'''

class PohamHandle:
    quantity = 0
    
    def leftTurn(self, quantity):
        self.quantity = quantity
        return "좌회전"
    
    def rightTurn(self, quantity):
        self.quantity = quantity
        return "우회전"
