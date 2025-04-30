Data = ['<', '(', ')', '>', '<', '<']
stack = []
howmany = len(Data)
ans = 0
for i in range(howmany) :
    if Data[i] in '(<':
        stack.append(Data[i])
    elif stack and (Data[i] == ')' and stack[-1] =='(') or (Data[i] == '>' and stack[-1] == '<'):
        Data.pop()
    else : break

if not stack : ans = 1
print(ans)