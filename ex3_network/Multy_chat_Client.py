'''--------------------------------------------------------------
-------------------- 멀티 채팅 프로그래밍용 클라이언트 ----------------------
--------------------------------------------------------------'''

import socket
import threading
import sys

def handle(socket):
    while True:
        data = socket.recv(1024)
        if not data:continue
        print(data.decode('utf-8'))
        
# 표준출력 장치를 비워준다.(버퍼를 비워준다.)
sys.stdout.flush()

name = input('채팅 아이디 입력 : ')
cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cs.connect(('192.168.0.52', 7777)) 
cs.send(name.encode('utf-8')) 

th = threading.Thread(target=handle, args=(cs,))
th.start()

while True:
    msg = input('>>')
    sys.stdout.flush()
    if not msg:continue
    cs.send(msg.encode('utf-8'))
    
cs.close()