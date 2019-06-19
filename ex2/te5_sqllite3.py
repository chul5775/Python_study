'''--------------------------------------------------------------
--------------------- sqlite3를 사용해서 DB연동하기  --------------------
-----------------------------------------------------------------
<개요>
    python과 sqlite는 Type의 차이가 존재한다.
  
       --------------┬--------------
           python    │     sqlite
       --------------┼--------------
         - none      │   - null 
         - int       │   - INTEGER
         - float     │   - REAL
         - str       │   - TEXT
         - byte      │   - BLOB
        -------------┴---------------
--------------------------------------------------------------'''



import sqlite3
print(sqlite3.sqlite_version) #sqllite 버전 확인.

#conn = sqlite3.connect('example.db')
conn = sqlite3.connect(':memory:') # 연습용으로 쓰기 좋은 휘발성.


try:
    cur = conn.cursor() #SQL 처리를 위한 객체를 생성.
    
    # table 생성
    cur.execute('create table if not exists friends(name text, phone text, addr text)')
    
    # insert문 세가지 방법 
    cur.execute("insert into friends(name,phone,addr) values('한국인', '111-1111', '역삼동') ")
    cur.execute("insert into friends VALUES('고길동', '222-2222', '강남역12번 출구') ")
    cur.execute("insert into friends VALUES(?,?,?)", ('나길동', '333-3333', '강남역11번 출구') )
    
    mydata = ('신길동','444-4444','역삼 1동') # 튜플 Type으로 만들어서 밀어 넣어줬음.
    
    cur.execute("insert into friends VALUES(?,?,?)", mydata)
    conn.commit()
    
    #select
    cur.execute("select * from friends")
    print(cur.fetchone())   # 한개 레코드 읽기
#     print(cur.fetchone())
#     print(cur.fetchone())
#     print(cur.fetchone())
#     print(cur.fetchone())

    print(cur.fetchall())   # 전체 레코드 읽기
    
    print()
    cur.execute("select name, addr, phone from friends order by name asc")
    for r in cur:
#         print(r)
        print(r[0] + "님의 주소는 " + r[1] + ", 전화:" + r[2])
    
    
except Exception as e:
    print('err: ', str(e))
    conn.rollback()
    
finally:
    conn.close()
    
'''==============================================================='''  