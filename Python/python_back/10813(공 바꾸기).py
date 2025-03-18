n, m = map(int, input().split())
L = list(range(1, n + 1))

for _ in range(m):
    i, j = map(int, input().split())
    L[i - 1], L[j - 1] = L[j - 1], L[i - 1]

print(*L)