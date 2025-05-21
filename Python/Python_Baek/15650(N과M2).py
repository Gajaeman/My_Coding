n, m = map(int, input().split())
res = []

def dfs(start, depth):
    if depth == m:
        print(' '.join(map(str, res)))
        return
    for i in range(start, n + 1):
        res.append(i)
        dfs(i + 1, depth + 1)
        res.pop()

dfs(1, 0)