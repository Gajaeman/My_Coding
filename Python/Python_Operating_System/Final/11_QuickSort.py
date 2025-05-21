def quick_sort(_from, _to):
    if _from < _to:
        pivot = partition(_from, _to)
        quick_sort(_from, pivot-1)
        quick_sort(pivot+1, _to)

def partition(_from, _to):
    where = _from
    princess = Data[where]
    left = _from
    right = _to

    while left < right:
        while left < len(Data) and Data[left] <= princess : left += 1
        while right >= 0 and Data[right] > princess : right -= 1
        if left < right :
            Data[left], Data[right] = Data[right], Data[left]
    Data[where], Data[right] = Data[right], Data[where]
    return right

Data = [3,2,4,9,1,8,7,5]
quick_sort(0, len(Data)-1)

print(Data)