L = [list(map(int, input().split())) for _ in range(9)]
max_v = L[0][0]
cdn_y, cdn_x = 1, 1
for y in range(9):
    for x in range(9):
        if max_v < L[y][x]: 
            max_v = L[y][x]
            cdn_y, cdn_x = y+1, x+1
print(max_v)
print(cdn_y, cdn_x)