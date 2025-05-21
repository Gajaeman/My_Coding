MyMap = [list(input()) for _ in range(5)]
stack = []
num = []
cnt = 0

def is_near(p):
    for k in num:
        if k - 1 == p or k + 1 == p or k + 5 == p or k - 5 == p:
            return True

def dfs(start):
    global cnt
    if stack.count('Y') >= 4 : return
    elif len(stack) == 7 :
        cnt += 1
        return
    for i in range(start, 25):
        if not stack :
            stack.append(MyMap[i//5][i%5])
            num.append(i)
            dfs(i)
            stack.pop()
            num.pop()
        else :
            if is_near(i):
                stack.append(MyMap[i//5][i%5])
                num.append(i)
                dfs(i)
                stack.pop()
                num.pop()
    return

dfs(0)
print(cnt)