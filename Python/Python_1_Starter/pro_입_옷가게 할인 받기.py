#https://school.programmers.co.kr/learn/courses/30/lessons/120818
#머쓱이네 옷가게는 10만 원 이상 사면 5%, 30만 원 이상 사면 10%, 50만 원 이상 사면 20%를 할인해줍니다.
#구매한 옷의 가격 price가 주어질 때, 지불해야 할 금액을 return 하도록 solution 함수를 완성해보세요.

def solution(price):
    if 100000 <= price < 300000:
        price = price * 95 // 100
    elif 300000 <= price < 500000:
        price = price * 90 // 100
    elif 500000 <= price:
        price = price * 80 // 100
    
    return price


"""
# sol_1
def solution(price):
    discount_rates = {500000: 0.8, 300000: 0.9, 100000: 0.95, 0: 1}
    for discount_price, discount_rate in discount_rates.items():
        if price >= discount_price:
            return int(price * discount_rate)

# sol_2
def solution(price):
    return (100 - len([1 for k in [100000, 300000, 500000, 500000] if k<=price])*5) * price // 100

# sol_3
def solution(price):
    if price>=500000:
        price = price *0.8
    elif price>=300000:
        price = price *0.9
    elif price>=100000:
        price = price * 0.95
    return int(price)
"""
