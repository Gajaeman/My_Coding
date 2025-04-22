def GetSome(count):
    if count == 0: return
    print("재귀 호출 %d" %count)
    GetSome(count-1)

GetSome(3)