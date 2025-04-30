ICP = {'+':1, '-':1, '*':2, '/':2, '(':3}
ISP = {'+':1, '-':1, '*':2, '/':2, '(':0}
for x in range(1, 11):
    n = int(input())
    Data = [x for x in input()]
    Stack, Postfix = [], []
    for now in Data:
        if now.isdigit() : Postfix.append(now)
        elif now == ')':
            while Stack[-1] != '(':
                Postfix.append(Stack.pop())
            Stack.pop()
        else :
            if not Stack: Stack+=[now]
            elif ICP[now] > ISP[Stack[-1]] : Stack+=[now]
            else:
                while Stack and ISP[Stack[-1]] >= ICP[now]:
                    Postfix.append(Stack.pop())
                Stack += now
    while Stack:
        Postfix.append(Stack.pop())

    for now in Postfix:
        if now.isdigit():
            Stack.append(now)
        else :
            b = int(Stack.pop())
            a = int(Stack.pop())
            if now == '+': Stack.append(a + b)
            elif now == '-': Stack.append(a - b)
            elif now == '*': Stack.append(a * b)
            else : Stack.append(a / b)
    print(f"#{x} {Stack[0]}")