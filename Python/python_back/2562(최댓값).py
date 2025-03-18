L = []
for _ in range(9):
    L.append(int(input()))

print(max(L))
print(L.index(max(L))+1)