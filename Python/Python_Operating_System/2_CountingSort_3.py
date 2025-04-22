Data = [0,4,1,3,1,2,4,1]

maxData=max(Data)
Count = [0] * (maxData + 1)

for now in Data:
    Count[now] += 1

# 누적값 구하기
for i in range(1, len(Count)):
    Count[i] += Count[i-1]

print(Count)