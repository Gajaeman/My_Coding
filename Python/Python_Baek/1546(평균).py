n = int(input())
L = list(map(int, input().split()))
L = [x/max(L)*100 for x in L]
print(sum(L)/n)