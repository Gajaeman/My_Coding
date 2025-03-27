L = [[0] * 100 for _ in range(100)]
n = int(input())
for _ in range(n):
    p, q = map(int, input().split())
    for y in range(p, p+10):
        for x in range(q, q+10):
            L[y][x] = 1

res = 0
for y in range(100):
    for x in range(100):
        res += L[y][x]
print(res)