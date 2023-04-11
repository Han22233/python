'''
리스트 [] : ['김','이','박','최'] 

튜플 () : ('김','이','박','최')

딕셔너리(사전) {key : value} : 
fruits =  {'apple' : '사과', 'banana' : '바나나', 'carrot' : '당근'}
print(fruits['apple'])

집합 :
'''

# List 
# # int,float,string 다 가능 
'''
lst = [10,'20',30.5,40,50]
print(type(lst))
print(lst[0],"",lst[1],"",lst[len(lst)-1])
'''
'''
#빈 List 생성 후 원소 하나씩 추가 
list1=[]
#list2=list() # int()와 비슷한 기능 
list1.append("python")
list1.append("java")
list1.append("C++")
list1.append("python")
list1.append("python")
list1.append("python")
print(list1)

#for 1
for i in list1 : # == for i in ["python","java","C++"]
    print(i)

#for 2 
for index in range(len(list1)) :
    print(list1[index])

print(list1.count("python"))
print(list1.index("python"))

#List 수정 
list1[0] = "AI"
list1[2] = "IOT"
print(list1)

#리스트와 달리 튜플은 수정 불가 -> append, insert, 값 변경 안됨 
#튜플1 + 튜플2 = 튜플3은 가능 

list2 = list1[0:3:1] #list[0~2]
#print(list2)
list2 = list1[1:5:1]
#print(list2)
list2 = list1[1:len(list1):2]
#print(list2)
list2 = list1[2:6:3]
#print(list2)
list2 = list1[::-1]
#print(list2)

#list1의 일부를 list3에 대입 
list2 = list1[2:6:3] # == ['IoT','python']
list3=[1,2,3,4,5,6,7,8]

# 대입되는 방식이 다름 

#case1
list3[1]=list2
print(list3) 

#case2
list3[1:2]= list2
print(list3) 

'''

# list.append(value) : value를 해당 리스트 가장 끝에 삽입
# list.insert(index,value) : value를 index위치에 삽입 
# list.remove(value) : list의 value를 삭제 
# list.pop(index) : index위치의 value삭제 // index안쓰면 가장 끝 value 삭제  
# => return 값은 pop된 value
'''
food = []
#append는 리스트 가장 뒤에 삽입 
food.append("짜장면")
food.append("샌드위치")

#insert는 index를 이용하여 특정 위치에 삽입 가능 
print(food)
food.insert(0,"파스타")
print(food)
food.insert(2,"피자")
print(food)
'''
'''
#remove는 value로 접근 
food.remove("파스타")
print(food)

#pop은 index 지정 X시 가장 마지막 value를 pop , return 값은 pop된 value
print("food.pop : ",food.pop())
print(food)
print("food.pop : ",food.pop())
print(food)
'''
'''
print(food)
# extend는 list끝에 다른 list의 value를 삽입 
dessert = ['커피','케잌','와플']
food.extend(dessert) # food + dessert
print(food)

# list를 합쳐서 변수에 삽입 extend 처럼 사용 가능 
food_list = food + dessert
print(food_list)

# clear는 list의 모든 원소 삭제 
# food.clear()
# del food => food 변수 삭제, 내장 함수 
print(food)
#reverse는 원소의 순서를 거꾸로 정렬  
food.reverse()
print(food)
'''
'''
#내장함수는 실행 하고 변수에 안 넣으면 값 안바뀜 ex) int() divmod() 
#메소드는 바뀜 ex_ list.reverse(), list.pop()
#모두가 그런 건 아니지만 대체로 그럼 

fruit = ['carrot','dessert','banana','apple']
print(fruit)
print(sorted(fruit)) # 값이 일시적으로 변화 후 다시 원상복귀 , 내장함수
print(fruit)

fruit.sort() # 값이 오름차순으로 정렬되어 저장 , 클래스의 메소드
print(fruit) 
'''
#리스트 컴프리헨션 
#0~10까지 있는 List 생성
# 방법 1 
'''
l1 = [0,1,2,3,4,5,6,7,8,9,10]

#방법 2
l2=[]
for i in range(11) :
    l2.append(i)
print(l1,"\n",l2,)

#방법 3 리스트 컴프리헨션 
# 리스트 변수명 = [항목 for 변수 in  조건 ]
l3 = [ i for i in range(11)]
print(l3)

# 0~10까지의 숫자 제곱을 원소로 가지는 리스트를 작성하라 
l4 = [i**2 for i in range(11)]
print(l4)
l4 = [i*3 for i in range(11)]
print(l4)
l4 = ["hello" for i in range(11)]
print(l4)
# == for i in range(10) : 
#     l4.append("Hello")

#0~10까지의 숫자의 제곱을 리스트로 만들어라ㅏ.
# 짝수의 제곱만 넣어라
#l4 = [i**2 for i in range(0,11,2)]
l4 = [i**2 for i in range(11) if i%2 == 0]
print(l4)
'''
# l1 = [1,2,3,4,5] 
# l2 = l1 // 얕은 복사 
# 같은 [1,2,3,4,5]데이터의 주소 값을 가져 인자 변경 시 둘다 동시에 변경

#얕은 복사 shallow copy 
f1 = ['제육','파스타','짜장면','샌드위치']
wishlist = f1
print('f1       :',f1)
print('wishlist :',wishlist)

wishlist.pop() # == f1.pop()
print("after wishlist.pop()")
print('f1       :',f1)
print('wishlist :',wishlist)

# is : a와 b가 같은 메모리 영역을 참조하고 있는지 확인
# True 같은 메모리 참조, False 다른 메모리 참조
print(f1 is wishlist) 

#deep copy
f2 = f1[:] # == 0 ~ len()-1
f3 = list(f2) # 이것도 deep copy , .copy() method 혼자 공부하기 
print("deep copy")
print('f1       :',f1)
print('f2       :',f2)

f2.append('떡볶이')
print("after f2.append('떡볶이')")
print('f1       :',f1)
print('f2       :',f2)
print(f1 is f2)

f1.append('김밥')
print("after f1.append('김밥')")
print('f1       :',f1)
print('f2       :',f2)
print('wishlist :',wishlist)