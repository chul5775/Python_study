'''--------------------------------------------------------------
-------------------- 멀티 채팅 프로그래밍용 서버 --------------------------
--------------------------------------------------------------'''

import socket
import threading

ss= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss.bind(('192.168.0.52', 7777))
ss.listen(5)

print('채팅 서비스 시작...')
user = []

def ChatUser(conn):
    name = conn.recv(1024)
    data = '*^O^*' + name.decode('utf-8') + '님 입장!'
    print(data)
    
    try:
        for p in user:
            p.send(data.encode('utf-8'))
        
        while True:
            msg = conn.recv(1024)
            data = name.decode('utf-8') + '님 메세지: ' + msg.decode('utf-8')
        
            print('수신결과 : ', data)
            for p in user:
                p.send(data.encode('utf-8'))
                
        
    except :
        user.remove(conn)
        data = 'ㅠㅠ' + name.decode('utf-8') + '님 퇴장'
        print(data)
        if user:
            for p in user:
                p.send(data.encode('utf-8'))
        
        else:
            print('exit')

while True:
    conn, addr = ss.accept()
    user.append(conn)
    th = threading.Thread(target=ChatUser, args=(conn,))
    th.start()
    
    