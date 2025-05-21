import sys
n, m = map(int, input().split())
L = sorted(list(map(int, input().split())))
stack = []
def dfs(depth):
    if depth == m : 
        print(*stack)
        return
    for i in L:
        if i not in stack:
            stack.append(i)
            dfs(depth + 1)
            stack.pop()
    return

dfs(0)