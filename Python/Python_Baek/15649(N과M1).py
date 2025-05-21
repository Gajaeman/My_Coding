n, m = map(int, input().split())
visited = [False] * (n + 1)
result = []

def dfs(depth):
    if depth == m:
        print(' '.join(map(str, result)))
        return
    for i in range(1, n+1):
        if not visited[i]:
            visited[i] = True
            result.append(i)
            dfs(depth+1)
            result.pop()
            visited[i] = False

dfs(0)

''' #sol_2
n, m = map(int, input().split())

def dfs(path, mask):
    if len(path) == m:
        print(' '.join(map(str, path)))
        return
    for i in range(1, n + 1):
        if not (mask & (1 << i)): 
            dfs(path + [i], mask | (1 << i))

dfs([], 0)
'''



''' #sol_3
n, m = map(int, input().split())

def dfs(path, used):
    if len(path) == m:
        print(' '.join(map(str, path)))
        return
    for i in range(1, n + 1):
        if i not in used:  # 💥 중복 제거 → visited 대신 set
            dfs(path + [i], used | {i})  # 💥 path에 추가, used에 i 추가

dfs([], set())
'''