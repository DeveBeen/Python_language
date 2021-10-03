# 연도를 입력받으면, 윤년인지 아닌지 출력하는 프로그램

year = int(input()) # 연도를 입력

if year % 4 == 0: # 연도가 4의 배수
    if year % 100 == 0: # 연도가 100의 배수
        if year % 400 == 0: # 연도가 100의 배수이면서 400의 배수면 윤년
            print('Leap Year') # 윤년 출력
        else: # 연도가 100의 배수지만 400의 배수가 아닌 모든 연도는 평년
            print('Not Leap Year') # 평년 출력
    else: # 연도가 100의 배수가 아니면서 4의 배수인 연도는 윤년
        print('Leap Year') # 윤년 출력
else: # 연도가 4의 배수가 아니면 평년
    print('Not Leap Year') # 평년 출력
