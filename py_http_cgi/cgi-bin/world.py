s1 = "힘드니"
s2 = "늦게 와서 쩝쩝..."

print('Content-Type:text/html;charset=utf-8\n')

print('''
<html>
<body>
<h1>월드 문서</h1>
자료 출력{0},{1}
<br>
느낌이 오나요<br>
<img src="../images/test1.png" width='60%'/>
<br>
<a href='../main.html'>메인으로</a>
</body>
</html>
'''.format(s1, s2))