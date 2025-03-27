while True:
    L = sorted(map(int, input().split()))
    if L[2] == 0 : break
    if L[2] >= L[1] + L[0] : print("Invalid")
    elif L[0] == L[2] : print("Equilateral")
    elif L[0] == L[1] or L[1] == L[2] : print("Isosceles")
    else : print("Scalene")