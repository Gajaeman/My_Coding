# matrix = [[i*5 + j+1 for j in range(5)] for i in range(5)]
#1
'''
num = 0

for y in range(5):
    for x in range(5):
        num += 1
        print(num, end = ' ')
    print()
'''
#2
Data = [[1,2,3,4,5],[6,7,8,9],[10,11,12]]
for y in range(len(Data)):
    for x in range(len(Data[y])):
        print(Data[y][x], end = ' ')
    print()