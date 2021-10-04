# 비트연산자 AND, OR, XOR 계

a, b = map(int, input().split(' ')) # a, b '1' 또는 '0' 입력

def and_func(a, b): # and 비트연산자 계산 함수
    if a == 1 and b == 1: # 입력받은 두 bool값이 모두 True이면 True 아니면 False
        return 1
    else:
        return 0

def or_func(a, b): # or 비트연산자 계산 함수
    if a == 0 and b == 0: # 입력받은 두 bool값 중에 True가 하나라도 있으면 True 아니면 False
        return 0
    else:
        return 1

def xor_func(a, b): # xor 비트연산자 계산 함수
    if a == b: # 입력받은 두 bool값이 서로 같으면 False 아니면 True
        return 0
    else:
        return 1

print(and_func(a,b)) # and값 출력
print(or_func(a,b)) # or값 출력
print(xor_func(a,b)) # xor값 출력
