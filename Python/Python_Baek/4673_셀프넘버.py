#https://www.acmicpc.net/problem/4673
L1 = []; L2 = [x for x in range(1,10001)]
num = 1; k = 10; res = 0; 
while num <= 10000 :
    ans = num
    while ans >= 1 : 
        res += ans % 10
        ans //= 10
    res += num
    L1.append(res)
    num += 1
    res = 0;
L3 = list(set(L2) - set(L1))
L3.sort()
for x in L3 : 
    print(x)