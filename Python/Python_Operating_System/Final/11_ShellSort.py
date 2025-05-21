def shell_sort():
    howmany = len(Data)
    howfar = howmany >> 1
    while howfar > 0:
        for now in range(howfar, howmany):
            temp = Data[now]
            where = now
            compareWhere = where - howfar
            while compareWhere >= 0:
                if temp < Data[compareWhere] :
                    Data[where] = Data[compareWhere]
                    where -= howfar
                    compareWhere -= howfar
                else : break
            Data[where] = temp
        howfar >>= 1

Data = [9, 6, 8, 3, 1, 7, 5, 2, 4]
shell_sort()
print(Data)