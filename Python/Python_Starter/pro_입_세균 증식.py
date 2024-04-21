#https://school.programmers.co.kr/learn/courses/30/lessons/120910
#어떤 세균은 1시간에 두배만큼 증식한다고 합니다. 처음 세균의 마리수 n과 경과한 시간 t가 매개변수로 주어질 때 t시간 후 세균의 수를 return하도록 solution 함수를 완성해주세요.
def solution(n, t):
    return n*2**t

'''
#sol_1
def solution(n, t):
    return n << t
-> 2의 제곱배를 곱할 때 시프트 변환 이용 가능
-> 이진수로 n을 표현하고 뒤에 0을 t개 붙이는 개념
'''