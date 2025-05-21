def BFS(start):
    Queue = [start]
    Distance[start] = 0

    while Queue:
        here = Queue.pop(0)
        for next in MyMap[here]:
            if Distance[next] == -1:
                Queue.append(next)
                Distance[next] = Distance[here] + 1

for tc in range(1, 11):
    howmany, start = map(int, input().split())
    Data = list(map(int, input().split()))

    MyMap = [[] for _ in range(101)]
    for i in range(0, len(Data), 2):
        _from, _to = Data[i], Data[i+1]
        MyMap[_from].append(_to)

    Distance = [-1] * 101
    BFS(start)

    max_ = Distance[0]
    ans = 0
    for i in range(len(Distance)):
        if Distance[i] >= max_:
            max_ = Distance[i]
            ans = i

    print(f"#{tc} {ans}")


    '''
    def DFS(here):
    for next in MyMap[here]:
        if Distance[next] == -1 or Distance[next] > Distance[here] + 1:
            Distance[next] = Distance[here] + 1
            DFS(next)

for tc in range(1, 11):
    howmany, start = map(int, input().split())
    Data = list(map(int, input().split()))

    MyMap = [[] for _ in range(101)]
    for i in range(0, len(Data), 2):
        _from, _to = Data[i], Data[i + 1]
        MyMap[_from].append(_to)

    Distance = [-1] * 101
    Distance[start] = 0
    DFS(start)

    max_ = Distance[0]
    ans = 0
    for i in range(len(Distance)):
        if Distance[i] >= max_:
            max_ = Distance[i]
            ans = i

    print(f"#{tc} {ans}")    
    '''
