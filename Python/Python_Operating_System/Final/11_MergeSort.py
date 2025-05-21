def merge_sort(Data):
    if len(Data)<= 1:
        return Data
    mid = len(Data) >> 1
    left = Data[:mid]
    right = Data[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0
    while i<len(left) and j<len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

Data = [38,43,27,3,9,82,10]
print(merge_sort(Data))