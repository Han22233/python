'''
var = "python"
ch1 = var[0]
print(ch1)
print(var[0]," ",var[1]," ",var[2]," ",var[3])
print(var[-6]," ",var[0])
print("length of var : ",len(var))
print("PYTHON"[0])
'''

'''
p = "python"
print(p[1:5])
#index 1부터 5 직전 숫자인 4까지 index의 문자 표시
print(p[2:4])
print(p[0:3])
print(p[0:6])
print(p[0:len(p)])
'''

'''
p1 = "python"
print(p1[-5:-1])
print(p1[-4:-1])
print(p1[-6:-3])
print(p1[-6:-1])
print(p1[-len(p1):-1])
'''

'''
p2 = "python"
print(p2[:3])
print(p2[:4])
print(p2[1:])
print(p2[3:])
print(p2[:])
'''

'''
str = 'Monty Python'
print(len(str))
print(str[0:5],str[6:],str[6:12])
print(str[-12:-7],str[-6:],str[-6:0])
'''

'''
print('python'[1:5:3])
print('python'[::-1])
print('python'[5:0:-1])
print('python'[-1:-7:-1])
'''
'''
print("ab"+"\b"+"c")

print("hello\nworld")

print("aaaaaaa\vbbbbbbbb\vcccccccc")
print("aaaaaaa\"bbbbbbbb\"cccccccc")
'''
'''
str_var = "하하하하"
#type(str_var) => str
str_var.replace('하','호')
print(str_var.replace('하','호'))
print(str_var)

str_var2= "안녕하세요.파이썬. 파이썬 수업입니다."
str_var3 = str_var2.replace("파이썬","자바")
print("str_var2",str_var2)
print("str_var3",str_var3)

str_var4= "안녕하세요.파이썬. 파이썬파이썬. 파이썬파이썬. 파이썬파이썬. 파이썬파이썬. 파이썬 수업입니다."
print(str_var4.replace("파이썬","자바",5))
'''
test = input('실수를 입력 하세요')
test = test.replace('.','')
sum = int(test[0]) + int(test[1]) +int(test[2]) +int(test[3]) +int(test[4]) +int(test[5]) 

print(sum)