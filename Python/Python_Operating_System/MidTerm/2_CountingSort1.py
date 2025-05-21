Data = [0,4,1,3,1,2,4,1]

maxData=max(Data)
Count = [0] * (maxData + 1)

for i in range(len(Data)):
    Count[Data[i]] += 1
print(Count)