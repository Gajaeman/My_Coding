from collections import deque

n = int(input())
Data = deque([])

for _ in range(n):
    cmd = list(input().split(' '))
    if cmd[0] == 'push' : Data.append(int(cmd[1]))
    elif cmd[0] == 'pop': print(Data.popleft() if Data else -1)
    elif cmd[0] == 'size': print(len(Data))
    elif cmd[0] == 'empty' : print(0 if Data else 1)
    elif cmd[0] == 'front' : print(Data[0] if Data else -1)
    elif cmd[0] == 'back' : print(Data[-1] if Data else -1)