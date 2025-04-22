n = int(input())
L = [list(map(int, input())) for _ in range(n)]

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]
result = []

def dfs(y, x):
    global cnt
    if x < 0 or x >= n or y < 0 or y >= n:
        return
    if L[y][x] == 1:
        L[y][x] = 0
        cnt += 1
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            dfs(ny, nx)

for q in range(n):
    for p in range(n):
        if L[q][p] == 1:
            cnt = 0
            dfs(q, p)
            result.append(cnt)

result.sort()
print(len(result))
for k in result:
    print(k)