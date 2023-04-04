str = "파이썬은 파이썬은 파이썬은 파이썬은 파이썬은 파이썬은 파이썬은 파이썬은 파이썬은 "
sec_str = "파이썬은,파이썬은,파이썬은,파이썬은,파이썬은,파이썬은,파이썬은,파이썬은파이썬은 "

print('{}+{}={}'.format(2,3,5)) #각각의 중간 괄호에 뒤의 숫자가 들어감  
a,b = 5,10
print('{}+{}={}'.format(a,b,a+b)) #변수도 사용 가능 
print('{0}+{1}={2}'.format(a,b,a+b)) #a는 0번째 b는 첫번째 a+b는 두번째에 지정하여 넣기
print('{0:d}+{1:f}={2:f},{3:s}'.format(a,b,a+b,"Hi")) #0번째는 정수형으로, 1,2번째는 실수형으로 지정
# d => 정수형 f => 실수형 s=> 문자열 C언어 형식과 같음  
print('{2}+{0}={1}'.format(a,b,a+b))#a는 1번째 b는 2번째 a+b는 0번째에 지정하여 넣기
'''
print(str.split()) # 파라메터로 아무 것도 넣지 않으면 공백으로 나누어줌 
print(sec_str.split(','))
'''
'''
print(str.find("자바")) # -1 리턴
# print(str.index("자바")) 오류 발생

print(str.find("파이썬"))
print(str.find("파"))
print(str.find("썬"))

print(str.index("파이썬"))
print(str.index("파"))
print(str.index("썬"))
'''
'''
newstr = str.replace("파이썬은","자바는")
print("str :",str)
print("newstr :",newstr)

print("str.count('파이썬') : ", str.count("파이썬"))
print('->'.join(str))
'''


'''
value_false = False #True
print(type(value_false))

value_true = True
print(type(value_true))

print(int(value_false)) 
print(int(value_true))

print(bool(0),bool(1),bool(-1.2135),bool())
print(bool("sdasd"),bool("-1"),bool(""),bool(" "))
print(bool(5>10),bool(10>5),bool('a'>'b'),bool('b'>'a'))
'''