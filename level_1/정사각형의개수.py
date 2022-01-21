# 한 변의 길이가 N인 정사각형 모양의 격자판에서 크고 작은 모든 정사각형의 개수를 구하시오.

N = int(input()) # 격자판의 한 변의 길이 N 입력
total = 0 # 총 정사각형의 개수를 받을 변수 선언

for i in range(1,N+1): # 정사각형의 총 개수는 1부터 N까지의 제곱의 합
    total += i*i

print(total)
