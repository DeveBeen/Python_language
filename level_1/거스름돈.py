# 모든 물품의 값이 1000원 이하인 가게에서 물품을 구매 후 거스름돈 동전의 개수 (항상 내는 돈은 1000원)

price = int(input()) # 물건의 가격을 입력

five_hundred = int((1000 - price) / 500) # 500원 동전의 개수를 계산
hundred = int((1000 - price - 500 * five_hundred) / 100) # 100원 동전의 개수를 계산
five_ten = int((1000 - price - 500 * five_hundred - 100 * hundred) / 50) # 50원 동전의 개수를 계산
ten = int((1000 - price - 500 * five_hundred - 100 * hundred - 50 * five_ten) / 10) # 10원 동전의 개수를 계산

print('{} {} {} {}'.format(five_hundred, hundred, five_ten, ten)) # .format을 이용하여 출력
