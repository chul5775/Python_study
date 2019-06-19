'''--------------------------------------------------------------
--------------------------- DB 기본  -------------------------------
--------------------------------------------------------------'''


import sqlite3

def dbFunc(dbName):
    try:
        conn = sqlite3.connect(dbName)
        c = conn.cursor()
        
        c.execute("drop table if exists jikwons")
        c.execute("create table jikwons(id integer primary key, name text)")
        
        #insert
        c.execute("insert into jikwons values(1,'가나다')")
        
        #Tuple Data
        t_data = (2,'신기해') 
        c.execute("insert into jikwons values(?, ?)", t_data)

        t_data2 = 3, '신선해'
        c.execute("insert into jikwons values(?, ?)", t_data2)        

        t_data3 = ((4,'신기루'),(5,'김밥'))
        c.executemany("insert into jikwons values(?, ?)", t_data3)    
        
        # LIST DATA
        l_data = [6, '공기밥']
        c.execute("insert into jikwons values(?, ?)", l_data)    
        
        # DICT DATA (Key에 의한 맵핑이기 때문에, 칼럼명하고 같이 하면된다.)
        d_data = {'id':'7', 'name':'고래밥'}
        c.execute("insert into jikwons values(:id, :name)", d_data)    
        
        d_data2 = {'sabun':'8', 'name':'주먹밥'}
        c.execute("insert into jikwons values(:sabun, :name)", d_data2)    
        
        # update
        up_date = ('박치기', 7)  # ['박치기', 7]
        c.execute("update jikwons set name=? where id=?", up_date)
        
        # delete
        del_data = ('4')
        c.execute("delete from jikwons where id = ?", del_data)
        
        conn.commit()
        
        
        
        
        #select
        print('출력1')
        c.execute("select * from jikwons")
        for r in c:
            print(str(r[0]) + " " + r[1])
        
        print()
        
        print('출력2')
        c.execute("select * from jikwons where id <= 2")
        for r in c.fetchall():
            print(str(r[0]) + " " + r[1])

        print()
                    
        print('출력3')
        c.execute("select count(*) from jikwons")
        print("건수: " + str(c.fetchone()[0]))
           
    except Exception as e:
        print('err :' + str(e))
        conn.rollback()
        
    finally:
        conn.close()
        
if __name__ == '__main__':
    dbFunc('test.db')