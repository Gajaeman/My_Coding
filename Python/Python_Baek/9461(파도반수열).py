t = int(input())
for _ in range(t):
    n = int(input())
    dp = [1, 1, 1, 2, 2]
    if n > 5: 
        for i in range(5, n):
            dp.append(dp[i-5] + dp[i-1])
    print(dp[n-1])