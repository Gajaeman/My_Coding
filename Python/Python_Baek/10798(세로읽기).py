L = [list(input().strip()) for _ in range(5)] 

max_len = max(len(row) for row in L) 

for x in range(max_len): 
    for y in range(5):
        if x < len(L[y]):
            print(L[y][x], end='')
