def GetSome(n):
    s = 1
    for num in range(1, n + 1):
        s = s * num
    return s


a, b = 3, 4
getA = GetSome(a)
getB = GetSome(b)
print(getA * getB)