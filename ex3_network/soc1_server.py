'''--------------------------------------------------------------
---------------------- 컴퓨터 간 접속 상태 확인(서버 측) --------------------
-----------------------------------------------------------------
<개요>
        - 1회 접속 처리 시행.
--------------------------------------------------------------'''

from socket import *

serverSock = socket(AF_INET, SOCK_STREAM)
serverSock.bind(('127.0.0.1',9999)) # bind는 Tuple Type으로 접근해야 한다.
serverSock.listen(1) # 리스너를 설정. 1 ~ 5

print('server service 중...')

conn, addr = serverSock.accept() # 여기서 연결을 기다리는 중
print('client addr : ', addr)
print('from cilent message : ', conn.recv(1024).decode())

conn.close()
serverSock.close()

