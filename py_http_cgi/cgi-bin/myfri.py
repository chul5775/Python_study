import cgi

form = cgi.FieldStorage()

name = form["name"].value #String, name = request.getParameter("name")
tel = form["phone"].value
gender = form["gen"].value

print('Content-Type:text/html;charset=utf-8\n')

print('''
<html>
<body>
이름은 {0}, 전화는 {1}, 성별은 {2}
</body>
</html>
'''.format(name, tel, gender))
