def GetSome(a,b):
    if b == 1:
        return a
    halfpower = GetSome(a, b//2)
    if b&1:
        return halfpower * halfpower * a
    else : return halfpower * halfpower

print(GetSome(2, 11))