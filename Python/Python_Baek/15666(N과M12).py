n, m = map(int, input().split())
Data = sorted(list(map(int, input().split())))
stack = []

def dfs(depth):
    check = 0
    if depth == m:
        print(*stack)
        return
    for i in range(len(Data)):
        if check != Data[i] and (not stack or stack[-1] <= Data[i]):
            check = Data[i]
            stack.append(Data[i])
            dfs(depth+1)
            stack.pop()
    return

dfs(0)