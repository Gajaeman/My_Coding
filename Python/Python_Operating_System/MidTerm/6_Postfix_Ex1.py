Data = "3+4+2"
Stack = []
Postfix = []
for now in Data:
    if '0' <= now <= '9' : Postfix.append(now)
    else : #+
        Stack.append(now)
while Stack: Postfix.append(Stack.pop())
print(Postfix)