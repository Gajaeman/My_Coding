from itertools import combinations
from collections import deque

graph = [list(input()) for _ in range(5)]
answer = 0

def is_connected(comb):
    visited = [False] * 7
    q = deque([0])
    visited[0] = True
    count = 1

    while q:
        cur = q.popleft()
        y1, x1 = comb[cur] // 5, comb[cur] % 5
        for i in range(7):
            if not visited[i]:
                y2, x2 = comb[i] // 5, comb[i] % 5
                if abs(y1 - y2) + abs(x1 - x2) == 1:
                    visited[i] = True
                    q.append(i)
                    count += 1

    return count == 7

for comb in combinations(range(25), 7):
    s_count = 0
    for i in comb:
        y, x = i // 5, i % 5
        if graph[y][x] == 'S':
            s_count += 1
    if s_count < 4:
        continue
    if is_connected(list(comb)):
        answer += 1

print(answer)
