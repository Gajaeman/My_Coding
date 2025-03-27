n = int(input())
L = list(map(int, input().split()))
sd = int(input())

for _ in range(sd):
    gen, num = map(int, input().split())
    
    if gen == 1: 
        for x in range(num - 1, n, num):
            L[x] = 1 - L[x] # L[x] ^= 1로 개선

    elif gen == 2:
        idx = num - 1
        L[idx] = 1 - L[idx]
        k = 1
        while idx - k >= 0 and idx + k < n:
            if L[idx - k] != L[idx + k]:
                break
            L[idx - k] = 1 - L[idx - k]
            L[idx + k] = 1 - L[idx + k]
            k += 1

for i in range(0, n, 20):
    print(*L[i:i+20])
