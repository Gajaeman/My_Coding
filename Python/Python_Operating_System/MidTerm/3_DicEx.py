import sys
sys.stdin = open('3_input.txt', 'r')

def GetSome(s):
    d = {'대문자' : 0, '소문자' : 0}

    for letter in s:
        if 'A' <= letter <= 'Z':
            d['대문자'] += 1
        elif 'a' <= letter <= 'z':
            d['소문자'] += 1
    return d

Data = list(input())
ans = GetSome(Data)
print(f"대문자 개수 : {ans['대문자']}, 소문자 개수 : {ans['소문자']}")