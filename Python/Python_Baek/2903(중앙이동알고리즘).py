n = int(input())
L = [2]
for k in range(n):
        L.append(L[k]+2**k)
print(L[n]**2)