n, m, v = map(int, input().split())
graph = [[0 for _ in range(n+1)] for __ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

visited_dfs = [False] * (n+1)
visited_bfs = [False] * (n+1)

def dfs(x):
    visited_dfs[x] = True
    print(x, end=' ')
    for i in range(1, n+1):
        if graph[x][i] == 1 and not visited_dfs[i]:
            dfs(i)

def bfs(x):
    L = [x]
    visited_bfs[x] = True
    start = 0 
    while start < len(L):
        cur = L[start]
        start += 1
        print(cur, end=' ')
        for i in range(1, n+1):
            if graph[cur][i] == 1 and not visited_bfs[i]:
                visited_bfs[i] = True
                L.append(i)

dfs(v)
print()
bfs(v)


''' #sol_2
from collections import deque

n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    p, q = map(int, input().split())
    graph[p].append(q)
    graph[q].append(p)

for i in range(1, n + 1):
    graph[i].sort()

visited_dfs = [False] * (n + 1)
visited_bfs = [False] * (n + 1)

def dfs(v):
    visited_dfs[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited_dfs[i]:
            dfs(i)

def bfs(v):
    queue = deque([v])
    visited_bfs[v] = True
    while queue:
        now = queue.popleft()
        print(now, end=' ')
        for i in graph[now]:
            if not visited_bfs[i]:
                queue.append(i)
                visited_bfs[i] = True

dfs(v)
print()
bfs(v)
'''