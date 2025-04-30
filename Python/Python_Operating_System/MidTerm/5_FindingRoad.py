def DFS(here):
    Visited[here] = True
    for next in Graph[here]:
        if not Visited[next]:
            DFS(next)

for _ in range(10):
    V, E = map(int, input().split())
    Data = list(map(int, input().split()))

    Graph = [[] for _ in range(100)]
    Visited = [False] * 100

    for i in range(0, E*2, 2):
        _from, _to = Data[i], Data[i+1]
        Graph[_from].append(_to)

    DFS(0)

    print(f'#{V} {1 if Visited[99] else 0}')