n = int(input())
L = list(map(int, input().split()))

cal = result = L[0]

for i in range(1, n):
    cal = max(L[i], cal + L[i])
    result = max(result, cal)

print(result)