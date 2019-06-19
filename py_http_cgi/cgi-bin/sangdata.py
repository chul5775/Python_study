import MySQLdb

config = {
    'host':'127.0.0.1',
    'user':'root',
    'password':'123',
    'database':'test',
    'port':3306,
    'charset':'utf8',
    'use_unicode':True
}

print('Content-Type:text/html;charset=utf-8\n')

print("<html><body> ** 상품 자료 (python_) ** <p/>")
print("<table border = '1'>")
print("<tr><th>code</th><th>sang</th><th>su</th><th>dan</th></tr>")
try:
    conn = MySQLdb.connect(**config)
    cursor = conn.cursor()
    
    cursor.execute("select * from sangdata")
    datas = cursor.fetchall()
    
    for d in datas:
        print("""
        <tr>
            <td>{0}</td>
            <td>{1}</td>
            <td>{2}</td>
            <td>{3}</td>            
        </tr>
        
        """.format(str(d[0]), str(d[1]), str(d[2]), str(d[3])))
    
    
except Exception as e:
    print('err : ', e)
    conn.rollback()
    
finally:
    cursor.close()
    conn.close()
    
print("/<table>")
print("</body></html>")
