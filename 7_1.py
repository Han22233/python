# 리스트는 수정, 변경, 일부 원소 삭제 등 가능 
# 수정이 불가능한 항목들 => 튜플 
t1 = (1,2,3,4)
print(t1)

t2 = tuple() 
print(t2)

t3 = 1, #원소가 1 한 개인 튜플 정의 
print(type(t3))
print(t3)

# 튜플 메소드 두 개밖에 없음 ㅋㅋ index count 
t4 = 1,2,6,5,4,4,4,4
print(type(t4))

print(t4.index(5))
print(t4.count(4))

# 튜플의 연산 +,* , 원본은 그대로 놔두고 새로운 튜플을 생성 
t5 = 1,2,3,4,5 
t6 = 100,200,300 
print(t5+t6)
print(t5)
print(t6)

# sorted : 원본 안바뀜, lst.sort() : 원본 바뀜 
# 튜플에선 sorted 활용 가능
t7 = 'e','d','c','a','f'
print(t7)
print(sorted(t7)) # sorted의 인자로 튜플을 넣어도 리턴 값은 무조건 리스트 형태 []

