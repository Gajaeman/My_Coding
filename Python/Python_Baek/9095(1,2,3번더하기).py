num = int(input("몇 개 입력할래? : "))
for x in range(num) : 
    numx = int(input("숫자 입력 : "))
    mokx = numx // 3
    resx = numx % 3
    L = [3]*mokx + [resx]
    while 3 not in L : 
    
    print(L)


"""
import sys

def cal(num) : 
    mok3 = num // 3
    res3 = num % 3
    result = (mok3-1)*3
    if res3 == 2 : result += 2

    mok2 = num // 2
    res2 = num % 2
    result += (mok2-1)*2

    print(result)

N = int(sys.stdin.readline())
for x in range(N) : 
    Nx = int(sys.stdin.readline())
    cal(Nx)
"""