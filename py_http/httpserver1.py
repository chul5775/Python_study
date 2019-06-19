# Simple HTTPServer 작성
# SimpleHTTPRequestHandler : client 요청 처리.
from http.server import SimpleHTTPRequestHandler, HTTPServer
port = 7777

handler = SimpleHTTPRequestHandler
serv = HTTPServer(('127.0.0.1', port), handler)

print('웹 서비스 시작...')
serv.serve_forever()

