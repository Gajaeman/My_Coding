n, m = map(int, input().split())
stack = []
def back(depth):
    if depth == m : 
        print(*stack)
        return
    for i in range(1, n+1):    
        stack.append(i)
        back(depth+1)
        stack.pop()
    return

back(0)