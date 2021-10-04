# Bubble Sort 기법으로 입력한 숫자를 정렬해주는 프로그램

input_num = int(input()) # 입력할 숫자 개수를 입력

sort_list = list(map(int, input().split(' '))) # 위에 입력한 숫자 만큼 정렬할 숫자 입력

for i in range(0, input_num):
    for j in range(0, input_num-1):
        if sort_list[j] > sort_list[j+1]:
            sort_list.insert(j, sort_list[j+1])
            del sort_list[j+2]
        else:
            break
        j += 1
    i += 1

print(sort_list)
