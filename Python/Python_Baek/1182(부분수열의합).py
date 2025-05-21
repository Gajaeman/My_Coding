n, s = map(int, input().split())
data = list(map(int, input().split()))
cnt = 0

def dfs(index, total):
    global cnt
    if index == n:
        if total == s:
            cnt += 1
        return
    dfs(index + 1, total + data[index])
    dfs(index + 1, total)

dfs(0, 0)

if s == 0:
    cnt -= 1

print(cnt)