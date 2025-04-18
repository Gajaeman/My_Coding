def DFS(here):
    Visited[here] = True
    for next in MyMap[here]:
        if not Visited[next]:
            if next == 99 : print(f'#{V} 1')
            else : DFS(next)

for _ in range(10):
    V, E = map(int, input().split())
    Data = list(map(int, input().split()))

    MyMap = [[] for _ in range(100)]
    Visited = [False] * 100

    for i in range(0, E*2, 2):
        _from, _to = Data[i], Data[i+1]
        MyMap[_from].append(_to)
    

    DFS(0)
    if Visited[99] == False : print(f'#{V} 0')