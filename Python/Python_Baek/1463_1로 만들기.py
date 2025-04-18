import sys
num = int(sys.stdin.readline())
dp = [0] * (num + 1)

for x in range(2, num + 1):
    dp[x] = dp[x - 1] + 1
    if x % 2 == 0:
        dp[x] = min(dp[x], dp[x // 2] + 1)
    if x % 3 == 0:
        dp[x] = min(dp[x], dp[x // 3] + 1)

print(dp[num])


''' # 또 틀림
num = int(input("입력 : "))
dp = [0, 0, 1, 1, 2, 3, 2]
for x in range(7, num+1) : 
    if x % 3 == 0 : 
        dp.append(dp[x//3] + 1)
    elif x % 2 == 0 : 
        dp.append(dp[x//2] + 1)
    else : dp.append(dp[x-1] + 1)
print(dp[num])
'''

''' # 틀림
num = int(input("입력 : "))
count = 0

while num > 1 : 
    count += 1
    if (num-1) % 3 == 0 : 
        num -=1    
    elif num % 3 == 0 : 
        num //= 3
    elif num % 2 == 0 : 
        num //= 2
    else : num -= 1
print(count)
'''