price = int(input())
count = int(input())
total = 0
for _ in range(count):
    a, b = map(int, input().split())
    total += a*b
print("Yes") if price == total else print("No") 

"""
import sys

price = int(sys.stdin.readline().strip())
count = int(sys.stdin.readline().strip())
total = sum(int(a) * int(b) for a, b in (sys.stdin.readline().split() for _ in range(count)))
print("Yes" if price == total else "No")
=> 하나의 프린트문 안에서 삼항연산자 사용 가능
"""