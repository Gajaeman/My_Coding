import sys
sys.stdin = open('12_KMPAlgorithmInput.txt', 'r')

def makePI():
    pi[0] = -1
    i, j = 0, 1

    while j < howmany - 1:
        if pattern[i] == pattern[j]:
            pi[j+1] = pi[j] + 1
            i += 1
        elif pattern[i] != pattern[j]:
            if pattern[0] == pattern[j]:
                pi[j+1] = 1
                i = 1
            elif pattern[0] != pattern[j]:
                pi[j+1] = 0
                i = 0
        j += 1

pattern = input()
text = input()
howmany = len(pattern)
pi = [0] * howmany
makePI()

Texti = 0
isDone = False

while Texti <= len(text) - len(pattern):
    k = 0
    for pti in range(howmany):
        if text[Texti] == pattern[pti]:
            k += 1
            pti += 1
            Texti += 1
        else : break
    if k == howmany:
        print(Texti - howmany)
        isDone = True
        break
    Texti = Texti + k - pi[k]
if not isDone : print("none")