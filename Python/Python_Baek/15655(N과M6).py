n, m = map(int, input().split())
Data = sorted(list(map(int, input().split())))
stack = []
def dfs(depth) : 
    if depth == m : 
        print(*stack)
        return
    for i in Data:
        if i not in stack and (not stack or i > stack[-1]) : 
            stack.append(i)
            dfs(depth+1)
            stack.pop()
    return

dfs(0)