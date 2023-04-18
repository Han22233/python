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
season = {1:'1월',2:'2월',3:'3월',4:'4월',5:'5월',6:'6월',
          7:'7월',8:'8월',9:'9월',10:'10월',11:'11월',12:'12월'}
print(season.pop(0)) #  index에 있는 item을 제거 
print(season.popitem()) # 제일 마지막에 있는 item 제거