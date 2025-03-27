n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

INF = float('inf')
dp = [[[INF]*3 for _ in range(m)] for _ in range(n)]

for x in range(m):
    for d in range(3):
        dp[0][x][d] = graph[0][x]

for y in range(1, n):
    for x in range(m):
        for d in range(3):
            nx = x + (d - 1)
            if 0 <= nx < m:
                for prev_d in range(3):
                    if d != prev_d:
                        dp[y][x][d] = min(dp[y][x][d], dp[y-1][nx][prev_d] + graph[y][x])

result = min(dp[n-1][x][d] for x in range(m) for d in range(3))
print(result)