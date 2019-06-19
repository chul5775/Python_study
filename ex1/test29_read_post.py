'''--------------------------------------------------------------
--------------------- FILE INPUT/OUPUT (2)-----------------------
--------------------------------------------------------------'''

'''------------------------- 1. 우편 번호 읽기 ----------------------
<순서>

 데이터 입력받기 => zipcode.txt파일 읽어오기 => 데이터 자르기(동만 검색할 수 있게)

<데이터자르기>

 split(chr(9))로 List형식으로 자른다. => startswith로 객체 자료와 동일한 데이터만 끌고온다.
     => 입맛에 맛게 한줄씩 출력 
     
--------------------------------------------------------------'''

try:
    dong = input('동 이름을 입력 :')
    print(dong)
    
    
    with open('zipcode.txt', mode = 'r', encoding='euc-kr') as f:
#         print(f.read())
        line = f.readline()
#         print(line)
        
        while line:
#             lines = line.split('\t')
            lines = line.split(chr(9))
#             print(lines)
            if lines[3].startswith(dong):
                # print(line)
                print(lines[0] + ' ' + lines[1] + ' ' + lines[2] + ' ' + 
                     lines[3] + ' ' + lines[4])
            line = f.readline()
    
    
except Exception as e:
    print('error : ', e)

'''==============================================================='''