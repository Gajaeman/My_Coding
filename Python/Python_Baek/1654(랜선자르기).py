k, n = map(int, input().split()) #k 보유개수 , n 필요개수
L = [int(input()) for _ in range(k)]
MaxLength = 0
for i in range(1, min(L)+1):
    if sum(x//i for x in L) >= n :
        MaxLength = i
print(MaxLength)