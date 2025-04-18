n = int(input())

prev = [0] * 10
for i in range(1, 10):
    prev[i] = 1

for _ in range(2, n+1):
    curr = [0] * 10
    for j in range(10):
        if j > 0:
            curr[j] += prev[j-1]
        if j < 9:
            curr[j] += prev[j+1]
        curr[j] %= 10**9
    prev = curr

print(sum(prev) % 10**9 if n > 1 else sum(prev))