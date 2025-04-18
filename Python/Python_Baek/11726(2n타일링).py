n = int(input())
DP = [1, 2]
for x in range(2, n):
    DP.append(DP[x-2] + DP[x-1])
print(DP[n-1] % 10007)