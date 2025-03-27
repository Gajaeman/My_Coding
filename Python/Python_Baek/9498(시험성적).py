score = int(input())
print('A') if score >= 90 else print('B') if score >= 80 else print('C') if score >= 70 else print('D') if score >= 60 else print('F')
#=> 삼항연산자 print('a') if ~ else ~ 연속 사용