# 입력받은 밑변과 높이를 이용하여, 삼각형의 넓이를 구하는 프로그램

base, height = map(int, input().split(' ')) # 밑변과 높이를 입력

def triangle_array(b, h): # 밑변과 높이를 입력하여 삼각형의 넓이 구하는 함수
    return (1/2 * b * h)

print(round(triangle_array(base, height), 1)) # 소수점 일의 자릿수까지만 출력
