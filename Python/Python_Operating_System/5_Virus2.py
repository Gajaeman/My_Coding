import sys
sys.stdin = open("5_VirusInput.txt", 'r')

def DFS(Zombie):
    global ans
    ans += 1
    Visited[Zombie] = True
    for next in MyMap[Zombie]:
        if not Visited[next] : DFS(next)

V = int(input())
E = int(input())

MyMap = [[] for _ in range(V+1)]

for _ in range(E):
    _from, _to = map(int, input().split())
    MyMap[_from].append(_to)
    MyMap[_to].append(_from)

Visited = [False] * (V+1)
ans = 0
DFS(1)
print(ans-1)