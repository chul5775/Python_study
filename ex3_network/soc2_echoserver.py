'''--------------------------------------------------------------
---------------------- 컴퓨터 간 접속 상태 확인(서버 측) --------------------
-----------------------------------------------------------------
<개요>
        - 서버가 계속 살아있음
--------------------------------------------------------------'''
import socket
import sys

HOST = ''
PORT = 8888

serverSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try : 
    serverSock.bind((HOST, PORT))
    print('서버 서비스 중...')
    serverSock.listen(5)    # 동시 접속 수.
    
    while(True):
        conn, addr = serverSock.accept() # 여기서 연결을 기다리는 중
        print('client info : ', addr[0], addr[1]) # 이렇게 List형식으로 주면, IP주소와 PORT번호를 따로 받는다.
        print('from cilent message : ', conn.recv(1024).decode())

        #송신
        conn.send(('from server : ' + str(addr[1]) + \
                   ' 너도 잘 지내라').encode('utf-8'))
        
        
except Exception as e:
    print('err : ', e)
    sys.exit()  # 프로그램의 강제 종료
    
finally:
    serverSock.close()
    conn.close()