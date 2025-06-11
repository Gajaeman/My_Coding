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

''' # deque Ver
from collections import deque

for tc in range(1, 11):
    length, start = map(int, input().split())
    L = list(map(int, input().split()))
    
    Data = [[] for _ in range(101)]
    visited = [0] * 101

    for i in range(0, length, 2):
        Data[L[i]].append(L[i+1])

    q = deque()
    q.append((start, 0))
    visited[start] = 1

    max_depth = 0
    result = start

    while q:
        now, depth = q.popleft()

        if depth > max_depth:
            max_depth = depth
            result = now
        elif depth == max_depth:
            result = max(result, now)

        for nxt in Data[now]:
            if not visited[nxt]:
                visited[nxt] = 1
                q.append((nxt, depth + 1))

    print(f"#{tc} {result}")
'''