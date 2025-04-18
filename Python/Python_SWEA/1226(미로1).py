x = [0, -1, 0, 1]
y = [1, 0, -1, 0]

def dfs(q, p):
    if Map[q][p] == 3:
        return True
    Map[q][p] = 1
    for k in range(4):
        nq = q + y[k]
        np = p + x[k]
        if 0 <= nq < 16 and 0 <= np < 16 and Map[nq][np] != 1:
            if dfs(nq, np):
                return True
    return False

for _ in range(10):
    tc = int(input())
    Map = [list(map(int, input())) for __ in range(16)]
    result = dfs(1, 1)
    print(f"#{tc} 1" if result else f"#{tc} 0")