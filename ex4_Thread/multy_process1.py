'''--------------------------------------------------------------
----------------- 멀티 프로세싱  문제 해결 (Pool) -------------------------
-----------------------------------------------------------------
<개요>
    - 파이썬에서 GIL(Global Inerpreter Lock)의 문제로 thread 기능을 제대로 구현 할 수 없다.
    - Multi Processing을 지원하는 Pool과  Process로 멀티태스킹을 구현
    
    - 제대로 된 멀티태스킹을 하려면 Pool이나 Process로 작업해주어야한다.(지향한다)
    - 때문에, threading은 잠깐잠깐 사용할 때에만 사용한다.(지양한다)
    
    - Pool : 입력값을 process 별로 건너건너 분배하여 함수실행을 병렬화 할 수 있다.
--------------------------------------------------------------'''

from multiprocessing import Pool
import time
import os

def func(x):
    print('값 ', x, '에 대한 작업 PID=', os.getpid())
    time.sleep(1)
    return x * x 

if __name__ == '__main__':
    p = Pool(3)
    startTime = int(time.time())
    
    '''
    for i in range(0, 10):
        print(func(i))
    '''
    
    print(p.map(func,range(0,10)))
    '''
    <결과>
            값  0 에 대한 작업 PID= 9432
            값  1 에 대한 작업 PID= 4136
            값  2 에 대한 작업 PID= 3988
            값  3 에 대한 작업 PID= 9432
            값  4 에 대한 작업 PID= 4136
            값  5 에 대한 작업 PID= 3988
            값  6 에 대한 작업 PID= 9432
            값  7 에 대한 작업 PID= 4136
            값  8 에 대한 작업 PID= 3988
            값  9 에 대한 작업 PID= 9432
        [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
            총 작업시간 :  4
    
    <설명>
            파이썬 에서는 이런식으로 건너건너 스레드를 사용 가능하다.
    ''' 
    
     
    endTime = int(time.time())
    print('총 작업시간 : ', (endTime - startTime))

    