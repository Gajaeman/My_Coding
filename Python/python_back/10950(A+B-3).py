count = int(input())
for x in range(count): #for 문에 문자 사용하면 메모리 소요 -> _사용
    a,b = map(int, input().split())
    print(a+b)

""" 시간 단축
import sys

count = int(sys.stdin.readline().strip())
for _ in range(count):
    a, b = map(int, sys.stdin.readline().split())
    print(a + b)
"""