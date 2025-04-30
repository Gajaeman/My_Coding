Data = '1+2*3+(4+5)/6'
Stack, Postfix = [], []
ICP = {'+':1, '-':1, '*':2, '/':2, '(':3}
ISP = {'+':1, '-':1, '*':2, '/':2, '(':0}

for now in Data:
    if now.isdigit() : Postfix.append(now)
    elif now == ')':
        while Stack[-1] != '(':
            Postfix.append(Stack.pop())
        Stack.pop()#'(' 스택에서 제거
    else : #+, -, *, /, (, )
        if not Stack: Stack+=[now]
        elif ICP[now] > ISP[Stack[-1]] : Stack+=[now]
        else:
            while Stack and ISP[Stack[-1]] >= ICP[now]:
                Postfix.append(Stack.pop())
            Stack += now
while Stack:
    Postfix.append(Stack.pop())
print(Postfix)