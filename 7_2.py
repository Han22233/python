# dictionary
# key : value 
# 1 : 'a' , 2 : 'b'
'''
d1 = {1001:'홍길동',1002:'김길동',1003:'박길동',1004:'고길동'}
# d1[0]과 같이 인덱스로는 참조 불가합니다. 
print(d1[1001])

# d2 = {}도 가능
# 강좌에 대한 dictionary  
# key와 value의 여러 개의 자료형은이  한 딕셔너리에 들어갈 수 있음 
d2 = dict()
d2['강좌명'] = '파이썬' # d2[key] = value
d2['개설 요일'] = '화요일'
d2['생성연도'] = 2003 
d2['수강생'] = ['김','이','박']
d2[12] = 'hi'

print(d2)
print(d2['수강생'])
print(len(d2))
'''
'''
# dictionary 생성 key:value 1:1월 ... ~ 12:12월 
# for문 사용하여 각각의 value를 print하여라 
season = {1:'1월',2:'2월',3:'3월',4:'4월',5:'5월',6:'6월',
          7:'7월',8:'8월',9:'9월',10:'10월',11:'11월',12:'12월'}
'''
'''
1) key 값이 숫자인 것을 활용 
for i in range(1,13) : 
    print(season[i],end=' ')
print()
2) season을 for문의 인자로 주었을 때는 key가 반환 
for a in season : 
    print(season[a],end=' ')
print()
'''

# dictionary methods 
'''
print(season.keys()) # dictionary의 모든 key 리스트 형태로 반환 
print(season.values()) # dictionary의 모든 value 리스트 형태로 반환
print(season.items()) # dictionary의 key,value로 구성된 튜플의 리스트 형태로 반환
'''
'''
3) seanson.keys() 활용
for i in season.keys() :
    print(i,end=' ') 
    print(season[i], end=' ')

4) season.values() 활용
for a in season.values() :
    print(a,end=' ')

5-1) season.items() 활용 
for i in season.items() : 
    print(i[1], end=' ')


#5-2) season.items() 활용
for k,v in season.items(): 
    print(k,end=' ')
    print(v,end=' ')    
'''
'''
season = {1:'1월',2:'2월',3:'3월',4:'4월',5:'5월',6:'6월',
          7:'7월',8:'8월',9:'9월',10:'10월',11:'11월',12:'12월'}
print(season.pop(0)) #  index에 있는 item을 제거 
print(season.popitem()) # 제일 마지막에 있는 item 제거
'''
# dictionary-tuple-list 변환 
# tuple - 변경불가, 수정 X (아메, 핫초코, 라떼)
# tuple -> list 유자차 추가 => tuple 변경 
# list -> tuple 수강신청 전 수강생 변경 => tuple
# tuple, list => dictionary (1,2,3,4) , (홍,김,박,이)
'''
seql = ['a','b','c','d','e']

# list에서 tuple로 변환 
seqt = tuple(seql)
print(seqt)
print(type(seqt))

# tuple에서 list로 다시 변환 
seql2 = list(seqt)
print(type(seql2))

# list에서 dictionary로 변환 
seqd = dict(enumerate(seql))
print(seqd)
print(type(seqd))

# zip 
# list,tuple이 여러개가 있을 때 튜플의 조합으로 된 하나의 리스트로 만듦 
# => [('1조', '홍', '최'), ('2조', '김', '박'), ('3조', '이', '정')] 
l1 = ['1조','2조','3조']
YA = ['홍','김','이']
YB = ['최','박','정']

z = zip(l1, YA, YB)
print(type(z))
print(z)
print(list(z))
#tuple(z)는 불가능 
print(tuple(zip(l1,YA,YB)))

# 개수가 다를 경우에 제일 짧은 리스트의 길이 만큼만 튜플 생성 , 전가복 , 국수나무, 짜장면은 무시 됨 
l10 = ['한식',    '양식']#,    '중식',  '분식'] 
l11 = ['전주식당','닥터로빈','전가복', '국수나무']
l12 = ['제육',    '파스타',  '짜장면']#,'돈까스']

lunchz = zip('ABCD',l10,l11,l12)
lunchl = list(lunchz)
print(lunchl)

for i in lunchl :
    print(i[0],i[1],i[2],i[3])

la = ['한식',    '양식',    '중식',  '분식'] 
lb = ['전주식당','닥터로빈','전가복', '국수나무']
lc = ['제육',    '파스타',  '짜장면','돈까스']
print(dict(zip(la,lb))) 
# print(dict(zip(la,lb,lc))) 불가능, dictionary는 key와 value 두 개의 값밖에 없기 때문  
print(dict(zip(la,(lb,lc)))) # 가능
'''
#enumarte는 하기와 같이 인덱스 붙여줌 
#        0        1        2         3
'''
l = ['전주식당','닥터로빈','전가복', '국수나무']
print(list(enumerate(l)))
print(dict(enumerate(l)))
'''

l21 = ['Vue.js','python','Oracle','Java','Arduino','C']
l22 = [313,214,213,315,210,313]

d20 = dict(zip(l21,l22))
while True :
    class_name = input('강의명을 입력하세요') 
    if class_name == 'quit' :
        print('프로그램 종료')
        break 
    else : 
        if class_name in d20.keys() : 
            print(d20[class_name]) 
        else : 
            continue
    