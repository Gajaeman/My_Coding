m = int(input())
n = int(input())
L = []

for x in range(m, n+1) : 
    cnt = 0
    for k in range(1, x//2 + 1):
        if x % k == 0 : cnt += 1
    if cnt == 1 : L.append(x)

if len(L) > 0 : 
    print(sum(L))
    print(L[0])
else : print(-1)