from collections import Counter

X, Y = zip(*(map(int, input().split()) for _ in range(3)))

cnt_x, cnt_y = Counter(X), Counter(Y)

res_x = next(k for k, v in cnt_x.items() if v == 1)
res_y = next(k for k, v in cnt_y.items() if v == 1)

print(res_x, res_y)

''' #sol 2
X, Y = [], []

for _ in range(3):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

count_x, count_y = {}, {}

for x in X:
    count_x[x] = count_x.get(x, 0) + 1
for y in Y:
    count_y[y] = count_y.get(y, 0) + 1

res_x = next(k for k, v in count_x.items() if v == 1)
res_y = next(k for k, v in count_y.items() if v == 1)

print(res_x, res_y)
'''

''' #sol 3
X, Y = zip(*(map(int, input().split()) for _ in range(3)))

x = next(i for i in X if X.count(i) == 1)
y = next(i for i in Y if Y.count(i) == 1)

print(x, y)
'''