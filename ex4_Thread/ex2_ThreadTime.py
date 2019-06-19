'''--------------------------------------------------------------
---------------------------- ex4_Thread(2) -----------------------------
-----------------------------------------------------------------
<개요>
        - time 
--------------------------------------------------------------'''

import time
from _ast import Or
now = time.localtime()
print(now)

print('현재는 {}년 {}월 {}일 {}시 {}분 {}초 '.format(now.tm_year, \
    now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec))


import threading

def showClock():
    now = time.localtime()
    print('현재는 {}년 {}월 {}일 {}시 {}분 {}초 '.format(now.tm_year, \
    now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec))

def my_run():
    while True:
        showClock()
        time.sleep(1)
        
th = threading.Thread(target=my_run)
th.start()
th.join()

print('bye')