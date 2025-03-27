n, m = map(int, input().split())
L = [x+1 for x in range(n)]
for _ in range(m) : 
    i, j = map(int, input().split())
    for k in range((j-i+1)//2) :
        L[i-1+k], L[j-1-k] = L[j-1-k], L[i-1+k]
print(*L)
'''
n, m = map(int, input().split())
L = list(range(1, n + 1))

for _ in range(m):
    i, j = map(int, input().split())
    L[i-1:j] = L[i-1:j][::-1]  
print(*L)
'''