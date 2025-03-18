'24시 시간 계산(45분 뺴기)'
print((h-1) % 24 if m < 45 else h, (m+15) % 60)
=> 나머지 이용하여 간락히 계산 가능

'두 개 이상의 자료 인풋 삽입'
a,b = map(int, input().split())

'삼항연산자' 
print('a') if ~ else ~ 연속 사용가능
print("Yes" if price == total else "No")
=> 하나의 프린트문 안에서 삼항연산자 사용 가능


'입력 시간 단축'
예를 들어, 100만 개의 숫자를 한 줄씩 입력받아야 한다면?
import sys
for _ in range(1000000):
    n = int(sys.stdin.readline().strip())
=> input보다 훨씬 빠름

'split'
split 사용하면 줄바꿈 문자는 자동으로 무시하여 리스트 생성

'특수문자 출력'
\출력하고싶으면 \\로 두개 이용
''출력하고싶으면 프린트문에 ""사용
-> \'로 출력도 가능

'정렬'
print(num.rjust(n)) -> 공백으로 채우기 / 왼쪽 ljust, 가운데 center
print(f"{text:>10}") -> 공백으로 채우기 / 왼쪽 :<, 가운데 :^
print("{:>10}".format(text)) -> 공백으로 채우기 / 왼쪽 :<, 가운데 :^
print(str.zfill(5)) -> 0으로 채우기 / 오른쪽 정렬 / 문자열만 사용가능

'프로그램 입력 끝나면 자동 종료(파일 끝까지 읽기)'
while True:
    try:
        a,b = map(int,file.readline().split())
    except:
        break
    print(a+b)

'try, except문에서 발생 오류 확인'
while True:
    try:
        a, b = map(int, input().split())
    except Exception as e:
        print("오류 발생:", e)  # 어떤 오류가 발생했는지 출력
        break
    print(a + b)
=> 오류 발생: not enough values to unpack (expected 2, got 0)

'리스트 안의 요소만 출력'
1. print(" ".join(map(str, L)))
2. print(*L)

'자연수 리스트 생성'
L = [x+1 for x in range(n)]
-> L = list(range(1, n + 1))

'리스트 값 한번에 교체 가능'
L[i - 1], L[j - 1] = L[j - 1], L[i - 1]

'리스트에서 특정 값 모두 삭제'
L = [x for x in L if x != 3]
L = list(filter(lambda x: x != 3, L))

'리스트 슬라이싱'
for _ in range(m) : 
    i, j = map(int, input().split())
    for k in range((j-i+1)//2) :
        L[i-1+k], L[j-1-k] = L[j-1-k], L[i-1+k]

=> 리스트 슬라이싱 활용
for _ in range(m):
    i, j = map(int, input().split())
    L[i-1:j] = L[i-1:j][::-1]


'여러 값 포함 리스트 생성'
#1 sys.stdin.readline().split()도 가능
L = list(map(int, input().split()))
print(L)

#2 리스트 컴프리헨션
L = [int(x) for x in input().split()]
print(L)

#3 numpy
import numpy as np
L = np.array(list(map(int, input().split())))
print(L)

'enurmerate 함수 : index와 value 반환'
s = "hello"
for idx, c in enumerate(s):
    print(f"Index: {idx}, Character: {c}")

'join 함수'
print(''.join(x * int(r) for x in s))
-> 빈칸을 기준으로 여러개의 문자열을 합하여 하나의 긴 문자열로 생성
-> 리스트 컴프리헨션과 함께 사용

'앞뒤 공백 제거'
s = str(input().strip())

'중간 공백 제거'
s = s.replace(" ", "")
s = "".join(s.split())
s = re.sub(r"\s+", "", s)  # 모든 공백 문자 제거

'딕셔너리'
dic[x] = dic.get(x, y) + k
-> dic의 키값 x가 존재하면 dic[x]반환
    존재하지 않으면 y값 반환 후 +k
max(dic, key=dic.get)	
딕셔너리의 키들 중에서, 키값이 가장 큰 키를 반환

'딕셔너리 한 번에 생성'
1. grades = dict.fromkeys(['A+', 'A0', 'B+', 'B0', 'C+', 'C0', 'D+', 'D0'], 0)
2. grades = {key: 0 for key in ['A+', 'A0', 'B+', 'B0', 'C+', 'C0', 'D+', 'D0']}
3. grades = {'A+': 5, 'A0': 3, 'B+': 8, 'B0': 2}  # 기존 딕셔너리
    grades.update({key: 0 for key in grades})

'2차원 배열'
print(*row)로 열 단위 출력 가능

'진법 변환'
n진법 숫자 a -> 10진법 변환
int(n, a)