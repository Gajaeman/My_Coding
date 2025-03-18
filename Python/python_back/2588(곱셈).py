a = int(input())
b = input()

a1 = a * int(b[2])
a2 = a * int(b[1])
a3 = a * int(b[0])
a4 = a * int(b)

print (a1, a2, a3, a4, sep='\n')

#=> sep = '\n'과 같이 스플릿처럼 사용 가능
"""런타임 에러
a,b = map(int, input().split())
print(a*(b%10))
print(a*(b//10%10))
print(a*(b//100))
print(a*b)
"""