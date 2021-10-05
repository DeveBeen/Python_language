# 입력한 수만큼 '*'을 역삼각형 모양으로 출력

input_num = int(input()) # 수를 입력

for i in range(0, input_num): # 입력한 수 만큼 for 구문으로 반복
    for j in range(0, input_num-i): # 입력한 수 - i 만큼 반복
        print('*', end='') # '*' 출력
    print()
