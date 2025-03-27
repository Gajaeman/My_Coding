L = list(range(1, 31))
for _ in range(1,29):
    num = int(input())
    if num in L : L.remove(num)
print(min(L))
print(max(L))