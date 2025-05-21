a, k = map(int, input().split())
Data = list(map(int, input().split()))
count = 0
result = -1

for i in range(1, a):
    key = Data[i]
    j = i - 1

    while j >= 0 and Data[j] > key:
        Data[j + 1] = Data[j]
        count += 1
        if count == k:
            result = Data[j + 1]
        j -= 1

    if j + 1 != i:
        Data[j + 1] = key
        count += 1
        if count == k:
            result = Data[j + 1]

print(result)