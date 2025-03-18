t = int(input())
money_list=[25, 10, 5, 1]
for _ in range(t):
    money = int(input())
    result = []
    for k in money_list:
        result.append(money // k)
        money %= k
    print(*result)