# 지역변수, 전역변수 
num = 100 # 전역변수, global variable 
print('Out of function num :',num)

def addone() : 
    num = 10 #지역 변수, local variable  
    print("addone()",num+1)
    print("addone() num : ",num)

addone()

print('Out of function num :',num)

def addone1() : 
    # 내부 function에서 num을 수정하지 않을 때 function 바깥 변수인 num 사용 가능  
    print("addone1()",num+1)
    print("addone1() num : ",num)

addone1()

# 내부 function에서 전역 변수를  사용하고 
# 변수 값을 수정하고 function이 끝나도 그 값이 반영되게 할 때 
def addone2() :
    global num # 전역 변수를 사용할 것을 선언, 전역 변수에 새로운 값 대입 가능 
    num = 2 
    print("addone1()",num+1)
    print("addone1() num : ",num)

addone2()

print('last num : ',num)
