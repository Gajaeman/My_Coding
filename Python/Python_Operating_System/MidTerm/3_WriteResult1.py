num = 62
MyList = []
MyList.append(100)
MyList.append(num)

while True:
    MyList.append(MyList[-2] - MyList[-1])
    if MyList[-1] < 0:
        break

for now in MyList:
    print(now, end=' ')