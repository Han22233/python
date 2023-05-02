# 인자의 갯수가 여러개인 경우 
# 변수명 앞에 * 작성시 파라메터 여러개 받을 수 있음 
def hello2(*names) : 
    #안녕 찍기 
    for i in names : 
        print('안녕,',i)
hello2('김','이','박','최','정',1,2,3)

# 여러개의 파라메터를 받아 파라메터의 합을 리턴하는 함수 
def sumAll(*nums) :
    sums = 0
    for i in nums :
        sums += i
    return sums
print("합 :",sumAll(1,2,3,4,5,6))

# list를 인자로 사용시 앞에 *를 붙여줌 
lst1 = [5,6,4,5,8]
print(sumAll(*lst1))

# dictionary를 인자로 사용시 앞에 **를 붙임, key와 value형태로 받는다는 뜻
coffee = {'아메리카노':2000,'라떼':3000,'티':2500}
def printmenu(**menus) : 
    for items in menus : 
        print(items, menus[items])
printmenu(**coffee)
printmenu(abc=1,bcd=2,cde=3) # 따옴표 생략 가능 

def func1(*num,**menu) : 
    nums = 0
    #num들의 합 
    for i in num : 
        nums += i 
    print('합은',nums)
    #menu를 출력 
    for items in menu : 
        print(items, menu[items])
func1(1,2,3,4,5,말차라떼=4500,버블티=3800,프라푸치노=5000)
func1(*lst1,**coffee)
func1(56,2,35645,**coffee)