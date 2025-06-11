import sys
sys.stdin = open("13_SWEA5177(BinaryHip).txt", 'r')

def insert_into_pQueue(pQueue, value):
    pQueue.append(value)
    where = len(pQueue) - 1
    while where > 1 and pQueue[where] < pQueue[where>>1]:
        pQueue[where], pQueue[where >> 1] = pQueue[where>>1], pQueue[where]
        where >>= 1

T = int(input())
for tc in range(T):
    N = int(input())
    Data = list(map(int, input().split()))
    pQueue = [0]

    for value in Data:
        insert_into_pQueue(pQueue, value)

    where = len(pQueue)-1
    total = 0
    while where > 1:
        where >>= 1
        total += pQueue[where]
    print(f'#{tc} {total}')