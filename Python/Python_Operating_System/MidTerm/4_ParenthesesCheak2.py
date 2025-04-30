pare = {'>':'<', ')':'(', '}':'{', ']':'['}
Data = ['<', '(', ')', '>', '<', '<']
stack = []
ans = 0

while Data:
    now = Data.pop(0)

    if now in pare.values():
        stack.append(now)
    elif stack and stack[-1] == pare[now]:
        stack.pop()
    else : break

if not stack : ans = 1
print(ans)