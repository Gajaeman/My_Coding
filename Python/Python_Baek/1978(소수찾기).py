n = int(input())
L = list(map(int, input().split()))
res = 0
for x in L :
    cnt = 0
    for k in range(1, x//2 + 1) :
        if x % k == 0 : cnt += 1
    if cnt == 1 : res += 1
print(res)