n = int(input())*2 - 1
save = n
while n >= 1 :
    print(' '*((save-n)//2), end = '')
    print('*'*n)
    n -= 2
n += 2
while n < save : 
    n += 2
    print(' '*((save-n)//2), end = '')
    print('*'*n)