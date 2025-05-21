n, m = map(int, input().split())
Data = sorted(list(map(int, input().split())))
stack = []
visited = [False]*n

def dfs(start):
    check = 0
    if len(stack) == m : 
        print(*stack)
        return
    for i in range(start, n):
        if visited[i] == False and check != Data[i] and (not stack or stack[-1] <= Data[i]):
            visited[i] = True
            check = Data[i]
            stack.append(Data[i])
            dfs(i)
            stack.pop()
            visited[i] = False
    return

dfs(0)