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
