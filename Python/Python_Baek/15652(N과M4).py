n, m = map(int, input().split())
stack = []
def back(num, depth):
    if depth == m : 
        print(*stack)
        return
    for i in range(num, n+1):    
        stack.append(i)
#       print('**', i, '/', depth + 1, '/', *stack)
        back(i,depth+1)
        stack.pop()
    return

back(1, 0)