# 함수란 ? 
# input을 주면 output이 나오는 것 

'''
input - 숫자 - num1
output - 숫자 - output_num
이런 기능을 하는 function - multi
'''
# 함수 정의  
def multi(num1) :
    output_num = num1*3
    print('여기는 multi 함수 안입니다.') 
    return output_num

# 함수 호출 
print(multi(10))


# hello 함수, 
# input - 사람 이름 두 개 입력 
# output - 안녕 1번 사람, 안녕 2번사람 

# 함수 선언 
def hello(name1='홍길동',name2='김길동') : 
    print('안녕,',name1)
    print('안녕,',name2)
# 함수 호출 
hello('이땡땡','김땡땡')
hello()

# 두 개의 숫자를 입력받아 두개의 합을 함수 내에서 출력하시오. 
# 함수 선언
# =로 default 파라메터 선언 가능 
# default 파라메터를 입력하여 에러 방지
def mysum(num1=1, num2=1) : 
    return num1+num2
print(mysum())
def mysum2(num1=1, num2=1) : 
    print("두 숫자의 합은 :",num1+num2)
# 함수 호출 
mysum2(8,3)
mysum2()