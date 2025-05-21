Data = [2,3,5,4,1]
for i in range(1, len(Data)):
    for j in range(len(Data)-i):
        if Data[j] > Data[j+1] : Data[j], Data[j+1] = Data[j+1], Data[j]
print(Data)