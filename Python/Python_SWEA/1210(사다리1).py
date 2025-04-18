dx = [-1, 1, 0]
dy = [0, 0, -1]

def isPossible(y, x):
    return 0 <= x < 100 and 0 <= y < 100 and MyMap[y][x] == 1

def GetSome(y, x):
    if y == 0:
        print(f"#{tc} {x}")
        return
    for dir in range(3):
        newY = y + dy[dir]
        newX = x + dx[dir]
        if isPossible(newY, newX):
            MyMap[y][x] = 0
            GetSome(newY, newX)
            return

for _ in range(10):
    tc = int(input())
    MyMap = [list(map(int, input().split())) for _ in range(100)]
    for x in range(100):
        if MyMap[99][x] == 2:
            startX = x
            break
    GetSome(99, startX)