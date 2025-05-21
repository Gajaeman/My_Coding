Data = [10, 20, 30, 50, 10]
isPalin = True
for now in range(len(Data)>>1):
    if Data[now] != Data[-1-now]:
        isPalin = False
        break
print(isPalin)