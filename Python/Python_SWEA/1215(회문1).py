def isPalin(y, x, dir):
    for i in range(howmany // 2):
        if dir == 0: 
            if grid[y][x + i] != grid[y][x + howmany - 1 - i]:
                return False
        else: 
            if grid[y + i][x] != grid[y + howmany - 1 - i][x]:
                return False
    return True

for tc in range(1, 11):
    howmany = int(input())
    grid = [list(input()) for _ in range(8)]
    ans = 0

    for y in range(8):
        for x in range(8 - howmany + 1):
            if isPalin(y, x, 0):
                ans += 1

    for x in range(8):
        for y in range(8 - howmany + 1):
            if isPalin(y, x, 1):
                ans += 1

    print(f"#{tc} {ans}")