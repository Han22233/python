# 내가 만든 hello 모듈
def hello_AI() :
    print('AI 모듈 메서드')

# 모듈 내에서도 소스 실행 가능 
# 단, import 할 때 같이 실행 됨 
# 이를 방지하기 위해 if문과 __name__ 사용 
if __name__ == '__main__' :
    print('오늘부터 갓생산다')
    hello_AI()
    print('__name__ : ',__name__)
# __name__ : 자신이 작성된 소스에서 print시 __main__이 출력됨 
#            다른 소스에서 print시 작성된 파일명(hello) 출력 
