# 입력한 수까지 모두 출력할 때, 3의 배수에는 'X'를 출력해주는 프로그램

input_num = int(input()) # 숫자 입력

def multiple_three(x): # 3의 배수 판별 함수
    if x % 3 == 0:
        return 'X' # 만약 입력받은 수가 3의 배수이면, 'X'값으로 리턴
    else:
        return x # 3의 배수가 아닌 경우는 그대로 리턴

i = 1 # while 변수용 i 선언

while i <= input_num: # 입력한 수까지 차례대로 반복문
    print(multiple_three(i), end = ' ')
    i += 1
