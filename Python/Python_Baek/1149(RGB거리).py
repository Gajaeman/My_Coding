n = int(input())
DP = [[0]*3 for _ in range(n)]
for i in range(n):
    r, g, b = map(int, input().split())
    if i == 0 : 
        DP[0][0], DP[0][1], DP[0][2] = r, g, b
    else : 
        DP[i][0] = min(DP[i-1][1] + r, DP[i-1][2] + r)
        DP[i][1] = min(DP[i-1][0] + g, DP[i-1][2] + g)
        DP[i][2] = min(DP[i-1][0] + b, DP[i-1][1] + b)
print(min(DP[n-1][0], DP[n-1][1], DP[n-1][2]))