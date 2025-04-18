num = int(input())
for tc in range(num):
    n, m = map(int, input().split())
    L = [list(map(int, input().split())) for _ in range(n)]
    result = []

    for y in range(n-m+1):
        for x in range(n-m+1):
            cal = 0
            for m_y in range(y, y+m):
                for m_x in range(x, x+m):
                    cal += L[m_y][m_x]
            result.append(cal)

    print(f'#{tc+1} {max(result)}')