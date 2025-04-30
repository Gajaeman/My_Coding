t = int(input())

for _ in range(t):
    freq = [0]*101
    num = int(input())
    score = list(map(int, input().split()))
    for x in score:
        freq[x] += 1
    m_freq = max(freq)
    result = max(i for i in range(101) if freq[i] == m_freq)

    print(f"#{num} {result}")