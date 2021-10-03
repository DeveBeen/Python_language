# 입력받은 두 정수의 나눗셈의 몫과 나머지를 출력하는 프로그램

a, b = map(int, input().split(' ')) # map(자료형, input)으로 변수를 입력받고, split() : 괄호안에 입력한 값이 값을 나누는 기준이되는 메소드이다.

value = int(a / b) # 입력받은 a, b의 값
remainder = int(a  - value * b) # 입력받은 a, b의 나머지

print('{} {}'.format(value, remainder)) # 출력
