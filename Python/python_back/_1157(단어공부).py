word = input().upper()
dic = {}

for x in word:
    dic[x] = dic.get(x, 0) + 1 

m = max(dic.values())
result = [k for k, v in dic.items() if v == m]

print('?' if len(result) > 1 else result[0])


''' # sol2
from collections import Counter

word = input().upper()
dic = Counter(word)
m = max(dic.values())

print('?' if list(dic.values()).count(m) > 1 else max(dic, key=dic.get))
'''