'''--------------------------------------------------------------
---------------------------- ex4_Thread Lock ------------------------
-----------------------------------------------------------------
<개요>
        - acquire(), release()
        - 두개 이상의 스레가 경쟁하고 있을때 ,
        - 공유 자원에 대해서 충돌을 방지해 주기 위해서 사용함.(다른 스레드는 대기상태로 들어감)
        
        - acquire를 하고 release를 해주지 않으면 Lock이 풀리지 않는다.
                
--------------------------------------------------------------'''

import threading, time

g_count = 0
lock = threading.Lock()

def threadCount(id, count):
    global g_count
    for i in range(count):
        lock.acquire()
        print('id %s ==> count:%s g_count:%s'%(id, i, g_count))
        g_count = g_count + 1
        
        lock.release()

for i in range(1, 6):    
    threading.Thread(target=threadCount, args=(i, 5)).start()
    
time.sleep(1)

print('final g_count : ', g_count)
print('bye')

