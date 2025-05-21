n, m = map(int, input().split())
Data = sorted(list(set(map(int, input().split()))))
stack = []

def dfs(depth):
    if depth == m : 
        print(*stack)
        return
    for i in range(len(Data)):
        stack.append(Data[i])
        dfs(depth+1)
        stack.pop()
    return

dfs(0)