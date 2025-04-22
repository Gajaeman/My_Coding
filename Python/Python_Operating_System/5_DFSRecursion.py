import sys
sys.stdin = open("5_Input.txt", 'r')

def DFS(here):
    print(here)
    Visited[here] = True
    for next in range(V+1):
        if not Visited[next] and MyMap[here][next]:
            DFS(next)

V, E = map(int, input().split())
MyMap = [[0 for _ in range(V+1)] for __ in range(V+1)]
Visited = [False] * (V+1)

for _ in range(E):
    _from, _to = map(int, input().split())
    MyMap[_from][_to] = 1
    MyMap[_to][_from] = 1

DFS(1)