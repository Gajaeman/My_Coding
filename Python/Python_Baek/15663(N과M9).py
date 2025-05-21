def dfs():
    check = 0
    if len(answer) == m:
        print(*answer)
        return
    for i in range(n):
        if check != Data[i] and visited[i] == False:
            answer.append(Data[i])
            visited[i] = True
            check = Data[i]
            dfs()
            answer.pop()
            visited[i] = False


n, m = map(int, input().split())
Data = sorted(list(map(int, input().split())))
visited = [False] * n
answer = []
dfs()