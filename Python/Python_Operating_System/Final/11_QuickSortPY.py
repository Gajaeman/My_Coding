def quicksort(Data):
    if len(Data) <= 1 :
        return Data
    pivot = Data[0]
    less, equal, greater = [], [], []
    for each in range(len(Data)):
        each = Data.pop()
        if each < pivot :
            less.append(each)
        elif each == pivot :
            equal.append(each)
        else : greater.append(each)
    return quicksort(less) + equal + quicksort(greater)

print(quicksort(Data = [3,2,4,9,1,8,7,5]))