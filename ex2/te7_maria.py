# 원격 데이터베이스 연동.
'''--------------------------------------------------------------
---------------- 원격 데이터베이스 연동(MySQL or MariaDB) --------------
--------------------------------------------------------------'''
import MySQLdb

# conn = MySQLdb.connect(host = '192.168.0.87', user = 'root', password='123', database='test')
# print(conn)
# conn.close

config = {
    'host':'127.0.0.1',
    'user':'root',
    'password':'123',
    'database':'test',
    'port':3306,
    'charset':'utf8',
    'use_unicode':True
}

try:
    conn = MySQLdb.connect(**config) #Dict
    cursor = conn.cursor()
    
    #insert
#     sql = "insert into sangdata values(%s,%s,%s,%s)"
#     sql_data = ('6','종이컵',100,200)
#     cursor.execute(sql, sql_data)

    
    #update
#     sql2 = "update sangdata set sang=%s, su=%s, dan=%s where code=%s"
#     sql_data2 = ('머그컵', 100, 2000,'6')
#     cursor.execute(sql2, sql_data2)

    
    #delete
    code = '6'
#   sql = "delete from sangdata where code=" + code #방법1
#   sql = "delete from sangdata where code={0}".format(code) #방법3
#   cursor.execute(sql)
 
    
    sql = "delete from sangdata where code=%s" #방법2
    cursor.execute(sql, (code,))
    
    conn.commit()
    
    #select
    sql = "select code, sang, su, dan from sangdata"
    cursor.execute(sql)
    
    print('< ----- select문 방법 1 ----- >')
    
    for data in cursor.fetchall():
        print('%s %s %s %s' %data)
    
    print('< ----- select문 방법 2 ----- >')
    
    for data in cursor:
        print(data[0], data[1], data[2], data[3])
    
    print('< ----- select문 방법 3 ----- >')
    for(a, b, c, d) in cursor: # 이거는 칼럼명이 아니기 때문에 그냥 편한대로 써도됨.
        print(a, b, c, d)
    
    print('< ----- select문 방법 4(정석대로 써도 상관없음./ ----- >')
    for(code, sang, su, dan) in cursor:
        print(code, sang, su, dan)
    
    
except Exception as e :
    print('err: ', str(e))
    conn.rollback()
    
finally:
    cursor.close()
    conn.close()

''' ---------------- <설명> ----------------
 
config = {
    'host':'127.0.0.1',
    'user':'root',
    'password':'123',
    'database':'test',
    'port':3306,
    'charset':'utf8',
    'use_unicode':True
}


- 이렇게 Dict Type으로 만들어서 사용시 ,
        보안을 위해 Pickle로 Dump처리를 해서 사용해야한다.
 

- 다른 호스트 주소로 들어가기 mysql -u root -h 127.0.0.1 -p

----------------------------------------'''