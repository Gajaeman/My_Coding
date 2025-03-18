n, m = map(int, input().split())

L1, L2 = [], []
L3 = [[0] * m for _ in range(n)]

for _ in range(n):
    L1.append(list(map(int, input().split())))

for _ in range(n): 
    L2.append(list(map(int, input().split())))

for y in range(n): 
    for x in range(m):
        L3[y][x] = L1[y][x] + L2[y][x]

for row in L3:
    print(*row)