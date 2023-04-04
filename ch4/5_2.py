#if문 
'''
if 조건 :
    실행문1
elif 조건 : 
    실행문 
else :
    실행문2
'''
'''
hour = 11
if hour < 12 :
    print("12시가 지나지 않았으니 오전입니다.")
elif hour < 18:
    print("12시가 지나고, 18시가 지나지 않았으니 낮입니다.")
else :
    print("18시가 지났으니 저녁입니다.")
'''

#장학금 
#score가 200보다 작으면 50만원을 줍니다 .
#score가 200이상 400미만이면 100만원, 400이상 500미만일 경우 1000만원을 줍니다.
# 
'''
score_str = input('점수는?')
score = int(score_str)
if score < 200 :
    print("50만원 획득")
elif score < 400 :
    print("100만원 획득")
else :
    print("1000만원 획득")
'''
'''
lunch = input('오늘 점심 메뉴는 ?(서브웨이/학식)')
if lunch == '서브웨이' :
    print("8호관 1층 서브웨이로 가세요")
elif lunch == '학식' :
    print('8호관 3층 학생식당으로 가세요')
else : 
    print('점심을 굶습니다')

answer = input('서브웨이 먹을래? (yes/no)')
if answer == 'yes' :
    print('8호관 1층')
else :
    answer = input('학식 먹을래? (yes/no)')
    if answer == 'yes' :
        print('8호관 3층')
    else :
        print('굶습니다')
'''

#반복문 
#for
'''
for i in 1,3,4,5,6,8 : 
    print(i)            
hap = 0
print("range 2 step")
for i in range(0,11,2) :
    print(i)
print("range 1 step ")
for i in range(11) :
    print(i)
    hap += i 
    print(i,"번째 합은",hap)
else : 
    print('for문의 조건이 더 이상 만족하지 않습니다')#for문의 else for문이 더 이상 조건이 만족하지 않을 때 실행  
    print('i가 range(11)에서 벗어남')
    print('for 문이 break나 continue로 종료된게 아니라 정상적으로 종료됐을 때만 출력')
print('range 1 step의 합은',hap)
'''

'''
while 조건 :
    수행문
'''
'''
i = 10
while i>5 :
    print(i,"는 5보다 크다.")
    i = i-1
#n=1부터 5까지 찍어보는 while문 
n = 1
while n < 6 :
    print(n,end='  **  ') 
    n = n + 1
else : 
    print('\nwhile문이 정상 종료되었습니다. 현재 i의 값은',i,"입니다")
'''
#놀이기구 탑승
#4명 탑승 가능, 5명은 안돼요 
#키 150이상만 탑승 가능 
#입력을 키를 받음 
#탑승 인원 체크, 키 체크 
#while문을 끝내는 조건은 ? 사람이 4명을 채웠는가 ?
'''
p = 0
while p<4 :
    people = input('키를 입력하세요 ')
 #   people_height = int(people)
    if people_height < 150 :
        print('탑승 불가합니다!')
    else :
        print('한 명 탑승하였습니다!')
        p += 1
        print('현재 탑승 인원은',p,'명입니다.')
else :
    print('놀이기구 정원이 다 찼습니다. 놀이기구가 출발합니다.')
'''
#continue , break
#반복문 중간에 반복을 더 이상 하지 않고 실행을 종료하는것
#반복문 안쪽에서 실행된다
#주로 if문 안쪽에서 사용됨

#input으로 입력을 받는데,
#무한반복
#exit이라는 값을 받으면 입력 받는 것을 종료
#apple을 받으면 단어를 입력하였습니다!부분을 출력하지 않습니다 

while True :
    str = input('단어를 입력하세요. (exit 입력 시 종료)')
    if str == 'exit' :
        print('exit을 입력 받았습니다. 프로그램이 종료됩니다.')
        break
    else: 
        if str == 'apple':
            print('apple을 입력 받았습니다. 문장이 실행되지 않습니다.')
            continue
        print('단어를 입력하였습니다! :',str)
    
    print('아직 while문이 돌아가는 중입니다!')

print('while 종료!')