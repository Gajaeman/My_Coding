V = int(input())
E = int(input())

MyMap = [[] for _ in range(V+1)]

for _ in range(E):
    _from, _to = map(int, input().split())
    MyMap[_from].append(_to)
    MyMap[_to].append(_from)

Visited = [False] * (V+1)
ans = 0
Infected = [1]

while True :
    if len(Infected) == 0:
        break
    Zombie = Infected.pop(0)
    if Visited[Zombie] == False:
        ans += 1
        Visited[Zombie] = True
        for next in MyMap[Zombie]:
            Infected.append(next)

print(ans-1)