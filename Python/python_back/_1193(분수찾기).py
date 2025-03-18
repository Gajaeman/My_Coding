num = int(input())
line = 1

while num > line:
    num -= line
    line += 1

a, b = (num, line - num + 1) if line % 2 == 0 else (line - num + 1, num)
print(f'{a}/{b}')