Data = [3, 2, 5, 4, 1]
def Ssort(Data, position=0):
    howmany = len(Data)
    if position >= howmany - 1 : return

    wheremin = position

    for now in range(position + 1, howmany):
        if Data[now] < Data[wheremin]:
            wheremin = now

    Data[position], Data[wheremin] = Data[wheremin], Data[position]
    Ssort(Data, position + 1)

Ssort(Data)
print(Data)