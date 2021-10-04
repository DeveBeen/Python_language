# '*'로 이루어진 피라미드를 출력하는 프로그램

floor = int(input()) # floor 층수 입력

for i in range(0, floor): # 층수 출력 for문
    for j in range(0, floor-i-1): # i층 한 줄 입력
        print(' ', end='')
    for k in range(0, 2*i + 1): # i층 한 줄 입력
        print('*', end='')
    print() # 층수 변경
