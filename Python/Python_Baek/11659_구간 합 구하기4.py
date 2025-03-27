n, m = map(int, input("개수, 횟수 : ").split())
L1 = list(map(int, input("리스트 : ").split( )))
L2, L3 = [], []

mysum = 0

for x in range(n) :
    mysum += L1[x]
    L2.append(mysum)
for y in range(m) : 
    i, j = map(int, input("번째").split( ))
    if i > 1 : L3.append(L2[j-1] - L2[i-2])
    else : L3.append(L2[j-1])
for x in L3 : print(x)