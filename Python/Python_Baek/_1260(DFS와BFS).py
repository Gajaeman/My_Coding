from collections import deque

n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for adj in graph:
    adj.sort()

visited_dfs = [False] * (n + 1)
def dfs(x):
    visited_dfs[x] = True
    print(x, end=' ')
    for nxt in graph[x]:
        if not visited_dfs[nxt]:
            dfs(nxt)

visited_bfs = [False] * (n + 1)
def bfs(x):
    q = deque([x])
    visited_bfs[x] = True
    while q:
        now = q.popleft()
        print(now, end=' ')
        for nxt in graph[now]:
            if not visited_bfs[nxt]:
                visited_bfs[nxt] = True
                q.append(nxt)

dfs(v)
print()
bfs(v)