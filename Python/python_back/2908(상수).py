num1, num2 = map(str, input().split())
if int(num1[::-1]) > int(num2[::-1]): print(num1[::-1])
else : print(int(num2[::-1]))