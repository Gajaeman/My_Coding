import sys
sys.stdin = open("5_Input.txt", 'r')

V, E = map(int, input().split())
MyMap = [[0 for _ in range(V+1)] for __ in range(V+1)]

for _ in range(E):
    _from, _to = map(int, input().split())
    MyMap[_from][_to] = 1
    MyMap[_to][_from] = 1

print(MyMap)