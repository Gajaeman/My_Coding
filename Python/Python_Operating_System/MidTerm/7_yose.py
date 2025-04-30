n, k = map(int, input().split())

Queue = []
for i in range(1, n + 1):
    Queue.append(i)

answer = []
count = 0

while len(Queue) > 0:
    count += k - 1
    if count >= len(Queue):
        count = count % len(Queue)

    removed = Queue.pop(count)
    answer.append(removed)

print("<", end='')
for i in range(len(answer)):
    if i == len(answer) - 1:
        print(answer[i], end='')
    else:
        print(answer[i], end=', ')
print(">")
