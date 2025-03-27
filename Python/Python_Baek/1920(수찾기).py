n = int(input())
L1 = sorted(list(map(int, input().split())))
m = int(input())
L2 = list(map(int, input().split()))
for x in L2:
    start, end = 0, n-1
    while True : 
        mid = (start + end) // 2
        if start > end :
            print('0')
            break
        elif L1[mid] == x : 
            print('1')
            break
        elif L1[mid] > x :
            end = mid - 1
        else : start = mid + 1