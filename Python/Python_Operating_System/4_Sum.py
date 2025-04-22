def GetSome(n):
    if n == 1 : return 1
    return n + GetSome(n-1)
print(GetSome(6))