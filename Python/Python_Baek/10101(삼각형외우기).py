L = sorted(int(input()) for _ in range(3))
if L[0] == L[2] and L[0] == 60 : print('Equilateral')
elif sum(L) == 180 :
    if L[0] == L[1] or L[1] == L[2] : print('Isosceles')
    else : print('Scalene')
else : print('Error')