'''--------------------------------------------------------------
------------------- 컴퓨터 간 접속 상태 확인(클라이언트 측) ------------------
--------------------------------------------------------------'''

from socket import *

clientSock = socket(AF_INET, SOCK_STREAM)
clientSock.connect(('192.168.0.87', 8888)) # server의 conn, addr = serverSock.accept()으로 감.

# 서버에게 자료 전송
clientSock.sendall(''.encode(encoding='utf-8', errors='strict'))

re_message = clientSock.recv(1024).decode()
print('수신자료: ', re_message)

clientSock.close()
