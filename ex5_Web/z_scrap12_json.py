import json

json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
print(json.dumps("\"foo\bar"))
print(json.dumps('\u1234'))
print(json.dumps('\\'))
print('\n---------------------')

print(json.dumps({"c": 0, "b": 0, "a": 0}, sort_keys=True))
data = {'b':3.4, 'a':0,'c':'hello word', 'd':{'sbs': 5}}
print(type(data))

json_data = json.dumps(data) #반환값 str Type
print('sort 전: ', json_data)

json_data = json.dumps(data, sort_keys= True) #반환값 str Type
print('sort 후: ',json_data)
print(type(json_data))

print('\n---------------------')
json_data2 =json.loads(json_data) 
print(json_data2)
print(type(json_data2))

print('\n---------------------')
json_data3 = {}

def readData(fileName):
    f = open(fileName, 'r', encoding='utf-8')
    lines = f.read()
    f.close()
    jdata = json.loads(lines)
    return jdata

def main():
    json_data3 = readData('ftest3.json')
#     print(json_data3)
    print(type(json_data3))
    d1 = json_data3['직원']['이름']
    d2 = json_data3['직원']['직급']
    d3 = json_data3['직원']['전화']
    print('이름:' + d1, ', 직급' + d2, ', 전화:' + d3)

    d4 = json_data3['웹사이트']['카페명']
    d5 = json_data3['웹사이트']['userid']
    print('카페명:' + d4 + ' ' + d5)

if __name__ == '__main__':
    main()








