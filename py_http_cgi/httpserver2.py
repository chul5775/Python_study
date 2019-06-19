#정적 요청 뿐 아니라, 동적 요청도 처리가 가능함.(CGIHTTPRe~~~를 써주면)
from http.server import CGIHTTPRequestHandler, HTTPServer
port = 8888

class Handler(CGIHTTPRequestHandler):
    cgi_directories=['/cgi-bin']

serv = HTTPServer(('127.0.0.1', port), Handler)

print('웹 서비스 시작...')
serv.serve_forever()


    