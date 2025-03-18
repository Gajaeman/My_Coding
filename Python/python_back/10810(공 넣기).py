import sys

n, m = map(int, input().split())
L = [0 for _ in range(n)]
for x in range(m) : 
    i, j, k = map(int, sys.stdin.readline().strip().split())
    for x in range(i-1, j):
        L[x] = k
print(*L)