st = [1, 1, 2, 2, 2, 8]
cur = list(map(int, input().split()))

for x in range(6):
    print(st[x]- cur[x], end = ' ')