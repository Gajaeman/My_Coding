def dfs(st):
    if st in visited:
        return
    visited.add(st)
    for i in Data[st]:
        dfs(i)
        
for tc in range(1, 11):
    length, start = map(int, input().split())
    L = [int(x) for x in input().split()]
    Data = list([] for x in range(101))
    visited = set()

    for i in range(0, length, 2):
        Data[L[i]].append(L[i+1])
    
    dfs(start)
    
    print(f"#{tc} {max(visited)}")