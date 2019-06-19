'''--------------------------------------------------------------
---------------------------- ex4_Thread -----------------------------
-----------------------------------------------------------------
<개요>
        - Tex5_Thread: Light weight process라고도 한다.
        - 스레드는 메인 프로세스와 병렬로 수행되는 미니 프로세스 이다.
        - 멀티 태스킹이 가능해 진다.
--------------------------------------------------------------'''

import threading, time

def run(id):
    for i in range(1, 11):
        print('id={} --> {}'.format(id, i))
#         time.sleep(0.5)

# thread를 이용하지 않은 경우
# run(1)
# run(2)        

# thread를 이용한 경우 : 병렬 처리
th1 = threading.Thread(target=run, args=('일',))
th2 = threading.Thread(target=run, args=('둘',))

# 스레드를 시작할때
th1.start()
th2.start()

# 메인스레드 대기 시킬때
th1.join()
th2.join()


print('프로그램 종료')




