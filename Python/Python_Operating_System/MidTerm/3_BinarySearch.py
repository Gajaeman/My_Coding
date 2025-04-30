Data = [2, 4, 7, 9, 11, 19, 23]
key = 7

start = 0
end = len(Data)-1
cnt = 0

while start <= end:
    mid = (start + end) // 2
    if Data[mid] == key :
        print("찾았다.")
        break
    elif Data[mid] > key:
        end = mid-1
    else : start = mid+1
    cnt += 1
print(cnt)