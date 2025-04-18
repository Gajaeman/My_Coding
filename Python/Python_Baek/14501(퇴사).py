n = int(input())
time = []
pay = []

for _ in range(n):
    t, p = map(int, input().split())
    time.append(t)
    pay.append(p)

dp = [0] * (n + 1)

for i in range(n - 1, -1, -1):
    if i + time[i] <= n:  
        dp[i] = max(pay[i] + dp[i + time[i]], dp[i + 1])
    else:  
        dp[i] = dp[i + 1]

print(dp[0])