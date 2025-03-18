n = int(input())
for x in range(1,10):
    print(n, '*', x, '=', n*x)

"""sys로 입력을 받으면 시간 단축
import sys

n = int(sys.stdin.readline().strip())
for x in range(1, 10):
    print(f"{n} * {x} = {n * x}")
"""