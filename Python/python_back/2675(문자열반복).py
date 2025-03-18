n = int(input())

for _ in range(n):
    r, s = input().split()
    for x in s:
        print(x*int(r), end='')
    print()

'''
#sol 2
n = int(input())

for _ in range(n):
    r, s = input().split()
    print(''.join(x * int(r) for x in s))
'''