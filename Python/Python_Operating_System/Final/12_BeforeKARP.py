text = [3,1,4,1,5,1,2]
pattern = 151
howmany = len(str(pattern))

for i in range(len(text) - howmany + 1):
    val = 0
    for now in range(i, i + howmany):
        val = val * 10 + text[now]
    print(val)
    if val == pattern : print("Found")