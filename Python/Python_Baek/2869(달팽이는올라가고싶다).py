a, b, v = map(int, input().split())
total = v - a
print(total // (a-b) + 1 if total % (a-b) == 0 else total // (a-b) + 2)