'''
import sys 
print(sys.builtin_module_names)

from math import gcd,fsum # math에서 gcd,fsum만 임포트
import math 
print(fsum([1,2,3])) # sum 후 float로 리턴 
print(gcd(25,15)) # 최대공약수 
print(math.ceil(5.25)) # 올림 

# pip install numpy 코드 실행 시 numpy 모듈 다운로드 
# 오류 발생 시 ctrl+shift+p 누른 후 python select interpreter 입력 
# base 선택 

import numpy as np #numpy를 np로 사용  
arrA = np.array([1,2,3,4,5])
arrB = np.array([6,7,8,9,10])

print(arrA+arrB) # arrA의 값과arrB의 값을 더해서 새로운 리스트 생성 
print(arrA-arrB)
print(arrA*arrB)
print(arrA/arrB)
'''
