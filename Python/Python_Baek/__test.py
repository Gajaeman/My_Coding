def GetSome(here):
    if here > Zombie : return
    for i in range(3) :
        next = here + Ability[i]
        if Time[next] > Time[here]+1 : #prunning
            Time[next] = Time[here]+1
            GetSome(next)
Ability = [0]*3
Shalala, Zombie = map(int, input().split())
Ability[0], Ability[1], Ability[2] = map(int, input().split())
Time = [987654321] * 1000
Time[Shalala] = 0
GetSome(Shalala)
print(Time[Zombie])
