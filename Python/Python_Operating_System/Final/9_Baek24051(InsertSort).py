n, k = map(int, input().split())
Data = list(map(int, input().split()))
cnt = 0

for i in range(1, n):
    key = Data[i]
    j = i-1

    while j >= 0 and Data[j] > key:
        Data[j+1] = Data[j]
        cnt += 1
        if cnt == k :
            print(Data[j+1])
            exit()
        j -= 1
    
    if j+1 != i:
        Data[j+1] = key
        cnt += 1
    if cnt == k :
        print(Data[j+1])
        exit()
print(-1)