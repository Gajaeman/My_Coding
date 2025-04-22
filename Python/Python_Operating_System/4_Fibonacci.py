def Fibo(n):
    if n == 0 or n == 1 : return 1
    return Fibo(n-1) + Fibo(n-2)

print(Fibo(10))