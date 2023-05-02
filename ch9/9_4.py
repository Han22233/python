# lambda function 
# function을 만드는데, 이름 짓기가 귀찮고, 실행문이 하나밖에 없거나 적을 것 같을 때 
# 익명함수 
# (lambda 파라메터 : 실행할 문장)(실제 파라메터)로 사용 

def addone(x) :
    return x+1 
print(addone(100))

# 위의 함수를 람다함수로 변환 시 
print((lambda x : x+1)(100))

# 파라메터가 여러개인 람다 함수 
print((lambda x,y : x+y)(2,5))

# lambda 함수를 활용하는 법 
# map,filter 함수 
# map(함수,input리스트) 
# list가 존재할 때, 리스트 안의 값들을 변화시키고 다른 리스트를 생성하고 싶을 때 사용 
lst1 = [1,2,3,4,5,6,7]
lst2 = list(map(lambda x : x+1 , lst1)) # lst1 대신 [1,2,3,4,5,6,7] 사용 가능 
print(lst2)


