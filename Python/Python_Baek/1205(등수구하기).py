n, score, p = map(int, input().split())

if n == 0:
    print(1)
    exit()

scores = list(map(int, input().split()))
scores = sorted(scores + [score], reverse = True)

rank = 1
for i in range(len(scores)):
    if scores[i] > score:
        rank += 1
    elif scores[i] == score:
        break

if len(scores) > p and scores[p] == score:
    print(-1)
else:
    print(rank)