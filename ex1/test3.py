'''------- 집합 자료형: List(배열과 유사) : 순서o 값변경 o -------'''
a = [1,2,3]
b = [10, a, 10.5, True, '문자열']
print(a)
print(b)


'''---------------- 1-1)slice(문자열 자르기 가능) ----------------'''

print(a[0], a[1])
print(b[0 : 2], b[2], b[1][1])

'''
<결과>
1 2
[10, [1, 2, 3]] 10.5 2
<설명> 
b[0 : 2] = [10, [1, 2, 3]]
b[2] = 10.5
b[1][1] = 2
'''

'''-------------------- 1-2)  --------------------'''
print(a[0], a[1])
print(b[0 : 2], b[2], b[1][1], b[1][:3])



'''-------------------- 1-3)수정이 가능하다  --------------------'''
print(a, id(a))
a[1] = 100
print(a, id(a))


'''------------------ 1-3)요소  추가 / 삭제  ------------------'''

fmaily = ['엄마', '아빠', '나']

fmaily.append('여동생') #추가 (값 1개 추가하기)
fmaily.insert(0, "할아버지") #추가 (원하는 주소에 추가하기)
fmaily.extend(['남동생', '이모', '고모']) #추가 (집합 자료 추가하기)
fmaily +=['조카', '삼촌'] #추가

fmaily.remove('여동생') #삭제 (값에 의한 삭제)
del fmaily[0] #삭제 (순서에 의한 삭

print(fmaily , ' ', len(fmaily))
print('------------------------')

'''-------------------- 1-4)리스트 뒤집기 --------------------'''
aa = ['123','34', '234']
print(aa)

aa.sort() # 리스트 정렬
print(aa)

aa.sort(key=int, reverse=True) # 리스트 뒤집기
# 여기서 reverse를 먼저 수행한 후 sort 해준다.
print(aa) 
print('------------------------')


'''================================================================='''

'''---- 2)집합 자료형 : tuple: 리스트와 유사하나 속도 빠름, read only, 순서o ----'''
'''

- tuple에서는 요소값이 하나밖에 없을 때에는 콤마(,)를 주어야한다.
    콤마를 주지 않으면 int로 판단해보린다. ex) k=(1, )

- 중괄호({})= set, 소괄호(())= tuple, 대괄호([]) = list 
- {:} = dict
'''

t = 'a','b','c','d'
print(t)

print(t[0:3])
# t[0] = 100 <== Error : 'tuple' object does not support item assignment
print(t)

q = list(t)
q[0] = 'mbc'
t = tuple(q)
print(t) 

t1 = (10, 20)
a, b = t1
b, a = a, b 
t2 = a, b 
print(t2)

# tuple은 read only 이기 때문에, 뭔가 하고 싶으면 형을 바꿔주면 된다.(list로)

'''================================================================='''



'''-------------------- 3) 집합 자료형 : set : 순서x, 중복 불가 --------------------'''

a = {1,2,2,3}
print(a, len(a))

'''
<결과>
{1, 2, 3} 3
<설명>
2가 한번만 나온 것으로 미루어 보아. (집합 자료형:set은 데이터를 Unique하게 만들어준다.) 
'''

# print(a[1])
'''
<결과>
Error : 'set' object is not subscriptable
<설명>
집합자료형 : set은 순서가 없다.
'''

b={3,4}
print('union : ', a.union(b))
print('intersection: ', a.intersection(b))
print('비교 연산자: ', a - b, a | b, a & b)

a.add(4)
a.update({2,5,6}) # update는 덮어 씌운다.
a.update((7,8)) #tuple
a.update([9,10]) #list
print(a)

a.discard(2) # 요소값 삭제
a.discard(2) 

a.remove(3) # 요소값 삭제
# a.remove(3)
'''
 -<설명> discard와 remove의 차이점은
         - discard는 있으면 지워주고 없으면 내버려 두지만.
         - remove는 책임감을 가지고 꼭 지워버리려고한다. (그래서 마지막 a.remove(3) = Error)
'''


print()

li =[1,2,2,3,1]
print(li)

s = set(li)
li = list(s)
print(li)


'''======================================================'''



'''-------------------- 4) 집합 자료형 : dict : {key:value} --------------------'''

mydic = dict(k1 =1, k2= 'kbs', k3 = 1.2)
print(mydic, type(mydic))

dic = {'파이썬': '뱀', '자바':'커피', '스프링':'용수철'}
print(dic, len(dic))

print(dic['자바'])
# print(dic['커피']) <- Key(파이썬, 자바, 스프링)로 value(뱀, 커피, 용수철을를 얻어오기때문에 이건 안됨.
# print(dic[0]) #err

print('dic.keys() : ', dic.keys())
print('dic.values() : ', dic.values())

dic['오라클'] = '디비' # 요소 추가
print(dic)

del dic['오라클'] # 요소 삭제 (키를 기준으로)
print(dic)


dic.clear()
print(dic)

'''======================================================'''


#Tip1) 