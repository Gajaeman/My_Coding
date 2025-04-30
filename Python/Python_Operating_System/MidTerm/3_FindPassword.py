import sys

n, m = map(int, input().split())
findP = {}
for _ in range(n):
    url, pw = sys.stdin.readline().split()
    findP[url] = pw

for _ in range(m):
    print(findP[input()])