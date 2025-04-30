import sys
sys.stdin = open('input.txt', 'r')

Visited = [False] * 8

def BFS(G, v):
    Queue = []
    Queue.append(v)
    Visited[v] = True

    while Queue:
        t = Queue.pop(0)
        print(t, end=' ')
        for u in range(1, 8):
            if G[t][u] == 1 and not Visited[u]:
                Queue.append(u)
                Visited[u] = True

MyMap = [[0]*8 for _ in range(8)]

for i in range(1, 8):
    row = list(map(int, input().split()))
    for j in range(1, 8):
        MyMap[i][j] = row[j-1]

BFS(MyMap, 1)
