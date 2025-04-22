６Data = '1+2*3-4/2'
Stack, Postfix = [], []
Priority = {'+':1, '-':1, '*':2, '/':2}

for now in Data:
    if '0' <= now <= '9' : Postfix.append(now)
    else : #+, -, *, /
        while Stack and Priority[Stack[-1]] >= Priority[now]:
            Postfix.append(Stack.pop())
        Stack.append(now)
while Stack:
    Postfix.append(Stack.pop())
print(Postfix)