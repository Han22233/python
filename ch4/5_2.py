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

lunch = input('오늘 점심 메뉴는 ?(서브웨이/학식)')
if lunch == '서브웨이' :
    print("8호관 1층 서브웨이로 가세요")
elif lunch == '학식' :
    print('8호관 3층 학생식당으로 가세요')
else : 
    print('점심을 굶습니다')