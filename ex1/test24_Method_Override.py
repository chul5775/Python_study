'''--------------------------------------------------------------
---------------------------- Method Override --------------------
--------------------------------------------------------------'''

class Parent:
    def PrintData(self):
        pass
    
class Child1(Parent):
    def PrintData(self):
        print('Child1에서 오버라이딩')
        
class child2(Parent):
    def PrintData(self):
        print('Child2에서 override')
        print('부모 메소드와 동일한 메소드를 재정의')

        
    def hi(self):
        print('Childe2의 고유 메소드')
        
print('\n<--- Child1 ---->\n')

c1 = Child1()
c1.PrintData()

print('\n<--- Child2 ---->\n')

c2 = child2()
c2.PrintData()

print('\n<--- 다형성(PolyMorPhism) 구사 (1) ---->\n')

par = Parent()
par = c1
par.PrintData()

print('\n<--- 다형성(PolyMorPhism) 구사(2) ---->\n')

par = c2
par.PrintData

abc = Parent()
abc = c1
abc.PrintData()

print('\n<--- 다형성(PolyMorPhism) 구사 (3) ---->')
print('<---     아무 변수 에게나 치환하면 된다.  ---->\n')
bbc = c1
bbc.PrintData()
bbc = c2
bbc.PrintData()
bbc.hi

print('\n<--- 다형성(PolyMorPhism) 구사 (4) ---->')
print('<---         List에 담아서 사용           ---->\n')

plist = [c1, c2]
for i in plist:
    i.PrintData()


'''============================================================'''
    