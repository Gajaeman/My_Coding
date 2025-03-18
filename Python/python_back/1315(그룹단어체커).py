n = int(input())
count = 0
for i in range(n):
    k = 0
    s = set()
    word = input()

    for j in word : 
        if j in s :
            if word[k-1] == word[k] : 
                s.add(j)
            else : 
                count -= 1
                break
        else : s.add(j)
        k += 1
    count += 1
print(count)