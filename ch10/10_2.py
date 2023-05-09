# 내가 만든 모듈 임포트하기 
# 같은 디렉터리 내부에 있을 때만 가능 
import hello as h 

print('=========================')
h.helloWorld()

print('__name__ in 10_2.py',__name__) # hello의 __name__과 비교해보기 

# 내가 만든 han 패키지 내부의 hello_data 모듈 임포트하기 
from han.dataanalysis import hello_data as hd
hd.helloWorld()