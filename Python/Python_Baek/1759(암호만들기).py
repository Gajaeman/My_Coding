l, c = map(int, input().split())
Data = sorted(input().split())
mo = {'a', 'e', 'i', 'o', 'u'}

stack = []

def dfs(start):
    if len(stack) == l:
        cnt_mo = sum(1 for ch in stack if ch in mo)
        cnt_ja = l - cnt_mo
        if cnt_mo >= 1 and cnt_ja >= 2:
            print(''.join(stack))
        return
    for i in range(start, c):
        stack.append(Data[i])
        dfs(i + 1)
        stack.pop()

dfs(0)