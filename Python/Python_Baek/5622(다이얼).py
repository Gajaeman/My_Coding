dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
word = input()
sum = 0
for x in word:
    for y in range(8):
        if x in dial[y]:
            sum = sum + y + 3
            break
print(sum)

'''
# sol2 : 딕셔너리 사용하면 시간복잡도 O(n^2) -> O(1)
dial_map = {
    'A': 3, 'B': 3, 'C': 3,
    'D': 4, 'E': 4, 'F': 4,
    'G': 5, 'H': 5, 'I': 5,
    'J': 6, 'K': 6, 'L': 6,
    'M': 7, 'N': 7, 'O': 7,
    'P': 8, 'Q': 8, 'R': 8, 'S': 8,
    'T': 9, 'U': 9, 'V': 9,
    'W': 10, 'X': 10, 'Y': 10, 'Z': 10
}

word = input()
print(sum(dial_map[x] for x in word))
'''