Data = [2,5,3,4,1]

for i in range(1, len(Data)):
    key = Data[i]
    j = i-1

    while key < Data[j] and j >= 0:
        Data[j+1] = Data[j]
        j -= 1

    Data[j+1] = key

print(Data)