import sys
sys.stdin = open('12_KMPInput.txt', 'r')

pattern = input()
howmany = len(pattern)
pi = [0] * howmany
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
print(pi)