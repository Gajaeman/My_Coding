n, b = map(int, input().split())
L = []
while n > 0 : 
    L.append(n%b)
    n //= b
print(*L.reverse())