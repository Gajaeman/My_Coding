L = []
for _ in range(10):
    num = int(input())
    L.append(num%42)
L = set(L)
print(len(L))