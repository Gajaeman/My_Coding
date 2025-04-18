n = int(input())
dp = [1, 1, 2]
for i in range(3, n):dp.append(dp[i-2] + dp[i-1])
print(dp[n-1])