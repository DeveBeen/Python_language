# 입력한 문자가 입력한 문자열에 몇 개 있는지 출력해주는 프로그램

input_string = input() # 문자열 입력
select_string = input() # 문자 입력
count = 0 # 카운트 변수 선언

for i in range(0, len(input_string)-1): # 문자열의 길이만큼 반복
    if input_string[i] == select_string: # if문에서 인덱싱 하여 문자와 비교
        count += 1 # 같을 때, 카운트 +1
        i += 1
    else:
        i += 1

print(count)
