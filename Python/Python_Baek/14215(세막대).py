L = sorted(list(map(int, input().split())))
while L[2] >= L[1] + L[0]:
    L[2] -= 1
print(sum(L))