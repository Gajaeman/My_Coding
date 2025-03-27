ans = 0
digit = 1
def GetSome(num):
    global ans
    global digit
    if num > 0:
        GetSome(int(num / 10))
        ans += (num % 10) * digit
        digit *= 10
    return

GetSome(321)
print(ans)