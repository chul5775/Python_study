'''--------------------------------------------------------------
----------------- 멀티 프로세싱  문제 해결 (Process) ---------------------
-----------------------------------------------------------------
<개요>
    - 제대로 된 멀티태스킹을 하려면 Pool이나 Process로 작업해주어야한다.(지향한다)
    - 때문에, threading은 잠깐잠깐 사용할 때에만 사용한다.(지양한다)
        
    - Process : Pool과는 달리 하나의 프로세스를 하나의 함수에 할당해 주는 방식
--------------------------------------------------------------'''

import os   
from multiprocessing import Process

def func():
    print('멀티 처리를 하고 싶은 내용 기술(대표적으로  Network)')

def doubler(num):
    result = num + 10
    func()
    proc = os.getpid()
    print('num:{}, result:{}, process:{}'.format(num, result, proc))
    
if __name__ == '__main__':
    nums = [1,2,3,4,5]
    procs = [] # join을 만나게 해주기 위헤서 리스트를 하나 만들어준다.(join = 현재 동작중인거 멈추기)
    
    for i, number in enumerate(nums):
        proc = Process(target=doubler, args=(number,))
        procs.append(proc)
        proc.start()
    
    for proc in procs:
        proc.join()
        