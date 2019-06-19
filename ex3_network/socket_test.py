'''--------------------------------------------------------------
---------------- Socket 클래스를 이용한 네트웤 프로그래밍 -------------------
--------------------------------------------------------------'''
import socket

print(socket.getservbyname('http','tcp'))
print(socket.getservbyname('telnet','tcp'))
print(socket.getservbyname('ftp','tcp'))

print(socket.getaddrinfo('www.naver.com', 80, proto=socket.SOL_TCP))
# 그냥 이야기 원래 네이버 주소 이름
# http://125.209.222.142:80/index.html



