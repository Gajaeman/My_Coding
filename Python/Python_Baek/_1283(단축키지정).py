n = int(input())
used = set()

for _ in range(n):
    words = input().split()
    found = False

    for idx, word in enumerate(words):
        ch = word[0].lower()
        if ch not in used:
            used.add(ch)
            words[idx] = f'[{word[0]}]{word[1:]}'
            found = True
            break

    if not found:
        for idx, word in enumerate(words):
            for j, ch in enumerate(word):
                if ch.lower() not in used:
                    used.add(ch.lower())
                    words[idx] = word[:j] + f'[{ch}]' + word[j+1:]
                    found = True
                    break
            if found:
                break

    print(' '.join(words))