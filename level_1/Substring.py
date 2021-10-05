# 문자열을 시작점을 기준으로 입력한 수의 길이만큼 출력하는 프롬그램

input_string = input() # 문자열을 입력

start, str_num = map(int, input().split(' ')) # 시작점과 문자길이를 입력

print(''.join(input_string[start-1:start+str_num-1])) # 시작점을 시작으로 시작점+문자길이를 끝으로 인덱싱하여 출력한다.
