# 입력한 문자열에서 공백을 모두 없애서 출력하는 프로그램.

input_string = list(input()) # 문자를 받아 리스트로 변환
i = 0 # while 구문 변수 i 선언

while i < len(input_string): # len함수로 문자열의 길이만큼 반복
    if input_string[i] == ' ': # ' '띄어쓰기가 된 원소는 제거
        del input_string[i]
        i += 1
    else:
        i += 1

print(''.join(input_string)) # .join(리스트): 리스트를 문자열로 출력
