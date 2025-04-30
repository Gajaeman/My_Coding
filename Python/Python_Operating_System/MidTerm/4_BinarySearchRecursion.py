def Bsearch(start, end):
    if start > end: return False
    mid = (start + end)//2
    if key == Data[mid] : return True
    elif key < Data[mid] : return Bsearch(start, mid-1)
    else : return Bsearch(mid+1, end)

Data = [2, 4, 7, 9, 11, 19, 23]
key = 7
print(Bsearch(0, len(Data)-1))