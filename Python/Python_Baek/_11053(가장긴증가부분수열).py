n = int(input())
L = list(map(int, input().split()))

dp = [1] * n 

for i in range(n):
    for j in range(i):
        if L[j] < L[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))