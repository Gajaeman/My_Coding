n = int(input())
L = []
cnt = 0
while n >= 3:
    if n % 5 == 0 : L.append(n//5+cnt)
    elif n % 3 == 0 : L.append(n//3+cnt)
    n -= 5
    cnt += 1
print(min(L) if L else -1)