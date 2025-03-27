num = 0
for _ in range(10):
    num += 1
    ans = 1
    n = int(input())
    txt = input()
    stack = []
    for i in txt :
        if i in '([{<' : stack.append(i)
        elif i in ')]}>' :
            if not stack : 
                ans = 0
                break
            elif i == ')' and stack[-1] == '(': stack.pop()
            elif i == ']' and stack[-1] == '[': stack.pop()
            elif i == '}' and stack[-1] == '{': stack.pop()
            elif i == '>' and stack[-1] == '<': stack.pop()
            else : 
                ans = 0
                break
        else : continue
    if stack : ans = 0
    print(f'#{num} {ans}')