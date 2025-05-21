from collections import deque

import sys
sys.stdin = open("9_YoseQueue.txt", 'r')

howmany, K = map(int, input().split())
Queue = deque(list(range(1, howmany+1)))
print('<', end = '')
while len(Queue) > 1 :
    for _ in range(K-1):
        Queue.append(Queue.popleft())
    print(Queue.popleft(), end = ", ")
print(Queue.popleft(), end = '')
print('>')