n = int(input())
L = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*k for k in range(1, n+1)]
dp[0][0] = L[0][0]
for y in range(1, n):
    for x in range(y+1):
        if x == 0 : dp[y][0] = dp[y-1][0] + L[y][0]
        elif x == len(dp[y])-1 : dp[y][x] = dp[y-1][x-1] + L[y][x]
        else : dp[y][x] = max(dp[y-1][x-1], dp[y-1][x]) + L[y][x]
print(max(dp[n-1]))