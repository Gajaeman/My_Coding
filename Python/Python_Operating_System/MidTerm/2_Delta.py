def isSafe(y, x):
    return 0<=y<5 and 0<=x<5

Data = [[1,2,3,4,5],
        [6,7,8,9,10],
        [11,12,13,14,15],
        [16,17,18,19,20],
        [21,22,23,24,25]]

whereY = -1
whereX = -1

for y in range(len(Data)):
    for x in range(len(Data[y])):
        if Data[y][x] == 6:
            whereY = y
            whereX = x
            break

dy = [-1,1,0,0]
dx = [0,0,-1,1]
for dir in range(4):
    newY = whereY + dy[dir]
    newX = whereX + dx[dir]
    if isSafe(newY, newX):
        print(Data[newY][newX])
