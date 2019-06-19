'''--------------------------------------------------------------
----------------- 클래스의 포함 관계 연습 : 냉장고에 물건 담기 ------------------
--------------------------------------------------------------'''

class Fridge:
    isOpened = False
    foods = []
    
    def open(self):
        self.isOpened = True
        print('냉장고 문 열기')
        
    def put(self, thing):
        if self.isOpened:
            self.foods.append(thing)
            print('냉장고 속에 음식이 들어감')
            self.f_list()
        else:
            print('냉장고 문이 닫혀 있어 음식을 담을 수 없어요.')
            
    def close(self):
        self.isOpened = False
        print('냉장고 문 닫기')

    def f_list(self):
        for f in self.foods:
            print('-', f.irum, f.expiry_date)
            
class FoodData:
    def __init__(self, irum, expiry_date):
        self.irum = irum
        self.expiry_date = expiry_date

f = Fridge()

print()
apple = FoodData('사과', '2019-5-31')
f.put(apple)
print('아뿔싸, 냉장고 문이 닫혀있어요')

f.open()
f.put(apple)
f.close()

print()

cola = FoodData('코카콜라', '2019-12-31')
f.open()
f.put(cola)
f.close()