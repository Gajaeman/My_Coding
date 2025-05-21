import sys
sys.stdin = open("9_BFS.txt", "r")

def BFS():
    while Queue :
        here = Queue.pop(0)
        Visited[here] = True
        print(here)
        for next in range(howmany + 1):
            if not Visited[next] and MyMap[here][next] :
                Parent[next] = here
                Distance[next] = Distance[here] + 1
                Visited[next] = True
                Queue.append(next)

howmany, E = map(int, input().split())
MyMap = [[0 for _ in range(howmany+1)] for __ in range(howmany+1)]

Visited = [False] * (howmany+1)
Parent = [-1] * (howmany+1)
Distance = [-1] * (howmany+1)

Queue = []

for _ in range(E):
    start, stop = map(int, input().split())
    MyMap[start][stop] = 1
    MyMap[stop][start] = 1

Queue.append(1)
Parent[1] = -1
Distance[1] = 0
BFS()

print(Distance)
print(Parent)