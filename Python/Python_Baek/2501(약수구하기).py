n, k = map(int, input().split())
L = [x for x in range(1, n+1) if n % x == 0]
print(L[k-1] if len(L) >= k else '0')