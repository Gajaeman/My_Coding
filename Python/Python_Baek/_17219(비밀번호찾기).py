import sys

n, m = map(int, input().split())
findP = {}
for _ in range(n):
    url, pw = sys.stdin.readline().split()
    findP[url] = pw

for _ in range(m):
    print(findP[input()])

''' #sol2
import sys

n, m = map(int, sys.stdin.readline().split())
findP = {url: pw for url, pw in (sys.stdin.readline().split() for _ in range(n))}
print("\n".join(findP[sys.stdin.readline().strip()] for _ in range(m)))
'''