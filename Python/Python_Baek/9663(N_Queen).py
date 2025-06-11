def dfs(y):
    if y == n :
        global res
        res += 1
        return
    for x in range(n):
        if issafe(y, x) : 
            matrix[y][x] = 1
            dfs(y+1)
            matrix[y][x] = 0

def issafe(y, x):
    for mul in range(1, y+1):
        for i in range(3):
            cal_y = y + dy[i]*mul
            cal_x = x + dx[i]*mul    
            if 0 <= cal_y < n and 0 <= cal_x < n :
                if matrix[cal_y][cal_x] == 1:
                    return False
    return True

n = int(input())
matrix = [[0]*n for _ in range(n)]
dx = [1,0,-1]
dy = [-1,-1,-1]    
res = 0
dfs(0)

print(res)


'''
#sol_2
def dfs(row):
    global res
    if row == n:
        res += 1
        return
    for col in range(n):
        if col in cols or (row + col) in diag1 or (row - col) in diag2:
            continue
        cols.add(col)
        diag1.add(row + col)
        diag2.add(row - col)
        dfs(row + 1)
        cols.remove(col)
        diag1.remove(row + col)
        diag2.remove(row - col)

n = int(input())
res = 0
cols = set()
diag1 = set()
diag2 = set()
dfs(0)
print(res)
'''