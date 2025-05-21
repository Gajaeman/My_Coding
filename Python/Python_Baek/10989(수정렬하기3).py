import sys
n = int(sys.stdin.readline())
Count = [0] * 10001

for _ in range(n):
    Count[int(sys.stdin.readline())] += 1

for num in range(1, 10001):
    for _ in range(Count[num]):
        print(num)