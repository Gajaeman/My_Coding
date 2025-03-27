n = int(input())
k = 1
while n != 1 : 
    k += 1
    while n % k == 0 : 
        n //= k
        print(k)

''' #sol 2 : 시간 단축(필요없는 연산 최소화)
n = int(input())
k = 2

while k * k <= n:  
    while n % k == 0:
        print(k)
        n //= k
    k += 1

if n > 1:
    print(n)
'''