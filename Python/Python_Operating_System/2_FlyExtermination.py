def isSafe(y, x, n):
    return 0 <= x < n and 0 <= y < n
t = int(input())

dyp = [0, 1, 0, -1]
dxp = [1, 0, -1, 0]
dym = [1, 1, -1, -1]
dxm = [1, -1, -1, 1]

for num in range(1, t+1):
    n, m = map(int, input().split())
    Data = [list(map(int, input().split())) for _ in range(n)]
    max_res = 0
    for y in range(n):
        for x in range(n):
            sum_p = sum_m = Data[y][x]

            for p in range(1, m):
                dyp_c, dym_c = [a * p for a in dyp], [b * p for b in dym]
                dxp_c, dxm_c = [c * p for c in dxp], [d * p for d in dxm]
                for i in range(4):
                    ny_p, nx_p = y + dyp_c[i], x + dxp_c[i]
                    ny_m, nx_m = y + dym_c[i], x + dxm_c[i]
                    
                    if isSafe(ny_p, nx_p, n):
                        sum_p += Data[ny_p][nx_p]
                    if isSafe(ny_m, nx_m, n): 
                        sum_m += Data[ny_m][nx_m]

            result= max(sum_p, sum_m)
            max_res = max(max_res, result)
    print(f"#{num} {max_res}")