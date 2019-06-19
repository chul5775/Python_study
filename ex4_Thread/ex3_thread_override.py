# thread를 상속받은 클래스

import threading, time, sys

class MyThread(threading.Thread):
    def run(self):
        for i in range(1, 11):
            print('id:{} ==> {}'.format(self.getName(), i))
            time.sleep(0.1)
    
ths = []
for i in range(2):
    th = MyThread()
    th.start()
    ths.append(th)

for th in ths:
    th.join()
    
print('bye')

print('-----------------')
class MyClock(threading.Thread):
    def run(self):
        while True:
            now = time.localtime()
            if 9 <= now.tm_hour <14:
                print('오전 근무 및 점심 시간')
            elif 14 <= now.tm_hour < 18:
                print('일해~~~~')
            else:
                print('자유시간')
                sys.exit()
                
                print('현재는{0}시{1}분{2}초'.format(now.tm_hour, now.tm_min, now.tm_sec))
                time.sleep(1)
                
                
mc = MyClock()
mc.start()
mc.join()

print('종료')