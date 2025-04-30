import sys
sys.stdin = open("6_CatchingZombie.txt", 'r')

Ability = [0]*3
Shalala, Zombie = map(int, input().split())
Ability[0], Ability[1], Ability[2] = map(int, input().split())
Time = [987654321] * 20
def GetSome(here): #2개의 사용 위치
    if here > Zombie : return
    for i in range(3) :
        next = here + Ability[i]
        if Time[next] > Time[here]+1 :
            Time[next] = Time[here]+1
            print(Time)
            GetSome(next)
Time[Shalala] = 0
if Shalala == Zombie : print(0)
else : GetSome(Shalala)
if Time[Zombie]!=987654321 : print(Time[Zombie])
else : print(-1)