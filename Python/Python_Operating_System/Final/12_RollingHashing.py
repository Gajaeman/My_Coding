text = [3,1,4,1,5,1,2]
pattern = 151
howmany = len(str(pattern))

digit = 10**(howmany-1)
val = 0
for now in range(howmany):
    val = val * 10 + text[now]

for i in range(1, len(text)-2):
    val -= digit*text[i-1]
    val*=10
    val+=text[i+howmany-1]

    if val == pattern : print(i)