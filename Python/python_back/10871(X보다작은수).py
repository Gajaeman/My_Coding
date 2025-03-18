n, x = map(int, input().split())
a = list(map(int, input().split()))
for k in range(n):
    if a[k] < x : 
        print(a[k], end = ' ')