cnt = int(input("숫자 개수 : "))
L = list(map(int, input("리스트 : ").split()))
x = int(input("x값 : "))
count = 0
L = sorted(L)

for k in range(x//2+1) :
    if k in L and x-k in L : count += 1
print(count)