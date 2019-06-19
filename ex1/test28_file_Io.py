'''--------------------------------------------------------------
--------------------- FILE INPUT/OUPUT (1) ----------------------
--------------------------------------------------------------'''

'''------------------------- 1. 파일 입/출력  ----------------------
<개요>

    1) 파일을 읽고 썼을때, 메모리 낭비를 방지하기위해 close를 꼭 해주어야 한다.
    
    - 이 때!, close를 매번 해주기 귀찮기 때문에  with를 사용.
    
    - open, write, r, w, a, readlines, close만 알아도 충분히 사용가능.

--------------------------------------------------------------'''
try:
    print('\n<--- 파일 읽기  --->\n')
    f1 = open('filetest.txt', 'r', encoding = 'utf-8')
    
    print(f1) # open 정보 보기
    print(f1.read()) # 파일 읽기.
    
    f1.close()
    
    print('\n<--- 파일 저장 --->\n')
    f2 = open('filetest2.txt', mode='w', encoding = 'utf-8')
    f2.write('My friend\n')
    f2.write('홍길동, 고길동')
    f2.close()
    print('저장 성공')
    
    print('\n<--- 파일 추가 --->\n')
    f2 = open('filetest2.txt', mode='a', encoding = 'utf-8')
    f2.write('\n신기해')
    f2.write('\n신선해')
    f2.close()
    print('저장 성공')
    
    print('\n<--- 한줄씩 읽기 --->\n')
    f3 = open('filetest2.txt', mode='r', encoding = 'utf-8')
    print(f3.readline())
    
    print('\n<--- 리스트 형식으로 담아주기 --->\n')
    aa = f3.readlines() # 리스트 타입에 담아준다.
    print(aa)
    f3.close()
    print('저장 성공')

    
    
except Exception as err:
    print('에러: ', err)

print('\n<--- close 한번에 처리하기 --->\n')



'''------------------------- 2. with를 이용한 저장하기----------------------
<개요>

    1) with를 통해서 파일 입출력 가능. (Close를 동시에 수행함)
    
    2) 객체를 파일로 저장 : 피클링(복합객체)

    - 객체를 파일에 쓸때에는 wb(write binary), 읽을때는 rb(read binary)로 할 수 있음.
    
    - pickle을 import 해준뒤 pickle.dump로 저장해준다.
    
-------------------------------------------------------------------'''
try:
    with open('filetest3.txt', mode = 'w', encoding='utf-8') as f4:
        f4.write('파이썬으로 문서 저장 \n')
        f4.write('with를 사용하면')
        f4.write('효과적')
      
    print('저장완료')   
    
    with open('filetest3.txt', mode = 'r', encoding='utf-8') as f5:    
        print(f5.read())
    
    print('\n<--- 객체를 파일로 저장 : 피클링(복합 객체 : object type으로 저장) --->\n')
    
    import pickle
    
    dicdata = {'tom' : '111-111', '길동' : '222-2222'}
    listdata = ['핸드폰', '모니터']
    tupledata = (dicdata, listdata) # 복합객체
    
    #쓰기
    with open('hello.dat', mode = 'wb') as f6: # wb = write binary
        pickle.dump(tupledata, f6)
        pickle.dump(listdata, f6)
    
    print('객체 저장 완료')
    
    # 읽기
    with open('hello.dat', 'rb') as f7:
        a, b = pickle.load(f7)
        print(a)
        print(b)
        
        c = pickle.load(f7)
        print(c)
        
except Exception as err2:
    print('에러2:', err2)


'''==============================================================='''