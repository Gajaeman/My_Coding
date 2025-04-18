n = int(input())
L = [int(input()) for _ in range(n)]

if n == 1:
    print(L[0])
elif n == 2:
    print(L[0] + L[1])
else:
    dp = [0] * n
    dp[0] = L[0]
    dp[1] = L[0] + L[1]
    dp[2] = max(L[0] + L[2], L[1] + L[2], dp[1]) 

    for x in range(3, n):
        dp[x] = max(dp[x-1], dp[x-2] + L[x], dp[x-3] + L[x-1] + L[x])

    print(dp[-1])