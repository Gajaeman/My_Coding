''' #Sol1_merge sort
n = int(input())
Data = []
for _ in range(n):
    Data.append(int(input()))

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
merge_sort(Data)
for x in result:
    print(result[x])
'''

''' #Sol2_quick_sort
n = int(input())
Data = []
for _ in range(n):
    Data.append(int(input()))

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
        while left< _to and Data[left] <= princess : left += 1						
        while right >= _from and Data[right] > princess : right -= 1						
        if left < right :						
            Data[left], Data[right] = Data[right], Data[left]
        else : break						
    Data[where], Data[right] = Data[right], Data[where]						
    return right						

quick_sort(0, len(Data)-1)	
for x in Data:
    print(Data[x])
'''

''' #Sol_3 Counting Sort
import sys
n = int(sys.stdin.readline())
Count = [0] * 10001

for _ in range(n):
    Count[int(sys.stdin.readline())] += 1

for num in range(1, 10001):
    for _ in range(Count[num]):
        print(num)
'''