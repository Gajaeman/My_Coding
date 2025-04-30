def isSafe(y, x):
    return 0 <= y < 5 and 0 <= x < 5

def myAbs(a):
    return a if a>0 else -a

Data = [[1,1,1,1,1],
        [1,0,0,0,1],
        [1,0,0,0,1],
        [1,0,0,0,1],
        [1,1,1,1,1]]

dy = [-1,1,0,0]
dx = [0,0,-1,1]

sum = 0
for y in range(5):
    for x in range(5):
        for dir in range(4):
            newY = y + dy[dir]
            newX = x + dx[dir]
            if isSafe(newY, newX):
                sum += myAbs(Data[y][x]-Data[newY][newX])
print(sum)