s = input()
for x in range(97, 123): 
    count = -1 
    for idx, c in enumerate(s):
        if ord(c) == x:
            count = idx 
            break
    print(count, end=" ")


'''
#sol 2
S = input()
abc ='abcdefghijklmnopqrstuvwxyz'

for i in abc:
    if i in S:
        print(S.index(i), end= ' ')
    else:
        print( -1, end =' ')

#sol 3
S = input()
check = [-1]*26
for i in range(len(S)):
    if check[ord(S[i])-97] != -1:
        continue
    else:
        check[ord(S[i])-97] = i
        
for i in range(26):
    print(check[i], end=' ')

#sol 4
S = input()
result = [-1] * 26

for idx, char in enumerate(S):
    if result[ord(char) - 97] == -1:
        result[ord(char) - 97] = idx

print(*result)
