'''--------------------------------------------------------------
------------------- 컴퓨터 간 접속 상태 확인(클라이언트 측) ------------------
--------------------------------------------------------------'''

from socket import *

clientSock = socket(AF_INET, SOCK_STREAM)
clientSock.connect(('127.0.0.1',9999)) # server의 conn, addr = serverSock.accept()으로 감.

# 서버에게 자료 전송
clientSock.sendall('안녕'.encode(encoding='utf-8', errors='strict'))
clientSock.close()
