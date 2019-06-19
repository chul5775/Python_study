'''--------------------------------------------------------------
--------------------- 내가 만든 모듈 활용하기 ---------------------------
--------------------------------------------------------------'''

print('--<실습1>--')
kor = 100
print('kor : ', kor)

import pacimport createModule.mymod1(pack.mymodcreateModulem)
list1 = [1,3]
list2 = [2,4,5]

pack.mymodcreateModulestPrint(list1, list2)
pack.mymodcreateModules()

'''------ <설명> ------
1. 같은 패키지에 있든, 다른 패키지에 있든 패키지명.모듈로 import 해준다.
------------------ '''

'''-------------------------------------------------------------'''
'''---------------------- 1. __name__과  __main__ -----------------'''
'''-------------------------------------------------------------'''

def abc():
    print('응용 프로그램 시작')

if __name__ == '__main__':
    #print('여기가 최상위 모듈이야~~')
    abc()

'''------ <설명> ------
1. 누군가의 의해서 호출되는 메소드들은  __main__ method를  만족하지 못한다.
------------------ '''



'''---------------------------------------------------'''
'''---------------------- 2.경로 지정하기  -----------------'''
'''--------------- from 패키지명 import 멤버 --------------'''
'''---------------------------------------------------'''
from pack import mymod1
mymod1.kbs()
print(mymod1.num)

from pack.mymod1 import kbs, mbc 
mbc()



'''---------------------------------------------------'''
'''------------- 3. 사용자가 만든 모듈을 이용한 연산. ------------'''
'''---------------------------------------------------'''

import pack.mymod2
print('합은', pack.mymod2.Hap(5, 3))

from pack.mymod2 import Hap
print('import createModule.mymod2
from pack.mymodcreateModuleport Cha
print('차는', Cha(5, 3))


'''-------------------------------------------------------------'''
'''------------- 3-1. Python37 -> Lib 폴더에 넣어서 사용. ------------'''
'''--- 현재  Lib의 Path가 걸려있기 때문에 패키지명을 따로 적어 줄 필요 없이 사용 가능. --'''
'''-------------------------------------------------------------'''

import mymod3
print('곱은', mymod3.Gop(5, 3))
from mymod3 import div
print('나누기는', div(5, 3))

'''==============================================================='''
