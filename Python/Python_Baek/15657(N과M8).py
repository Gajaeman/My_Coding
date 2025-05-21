n, m = map(int, input().split())
Data = sorted(list(map(int, input().split())))
stack = []

def dfs(start, depth):  
    if depth == m:
        print(*stack)
        return
    for i in range(start, n): 
        stack.append(Data[i])
        dfs(i, depth + 1)
        stack.pop()

dfs(0, 0)