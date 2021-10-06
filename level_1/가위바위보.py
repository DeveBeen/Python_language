# 5명이 가위바위보를 하였을 때, 승리한 사람의 수를 출력하는 프로그램

user_input = list(map(int, input().split(' '))) # 5명의 가위,바위,보 정보를 리스트로 받는다
rock = 0
scissors = 0
paper = 0

for i in range(0, 5): # 5회 반복을 통해 각각 가위, 바위, 보를 낸 사람의 수를 할당
    if user_input[i] == 1:
        scissors += 1
    elif user_input[i] == 2:
        rock += 1
    else:
        paper += 1

if rock == 5 or scissors == 5 or paper == 5: # 만약 모두가 같은 것을 냈다면, 이긴사람 수 : 0
    print(0)
elif rock * scissors * paper == 0: # 가위 또는 바위 또는 보를 낸 사람 중 하나라도 0명이라면, 승자가 생긴 것
    if rock == 0:
        print(scissors)
    elif scissors == 0:
        print(paper)
    else:
        print(rock)
else: # 다른 경우는 모두 무승부이므로 이긴사람 수 : 0
    print(0)
