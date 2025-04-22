Data = [3, 2, 5, 4, 1]
howmany = len(Data)

for position in range(howmany-1):
    wheremin = position
    for now in range(position+1, howmany):
        if Data[now] < Data[position] : wheremin = now
    Data[position], Data[wheremin] = Data[wheremin], Data[position]
print(Data)