def GetSome(here):
    global ans
    howmany = 4
    if here == howmany :
        ans += 1
        return
    if here > howmany : return
    GetSome(here+1)
    GetSome(here+2)
    ans = 0
    GetSome(0)
    print(ans)