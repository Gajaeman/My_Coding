n = 0
while n != -1 : 
    n = int(input())
    L = [x for x in range(1, n//2+1) if n % x == 0]
    if n == sum(L) : print(f"{n} = {' + '.join(map(str, L))}")
    elif n != -1 : print(f"{n} is NOT perfect.")