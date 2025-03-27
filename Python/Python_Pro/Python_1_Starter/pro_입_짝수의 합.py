#https://school.programmers.co.kr/learn/courses/30/lessons/120831
#정수 n이 주어질 때, n이하의 짝수를 모두 더한 값을 return 하도록 solution 함수를 작성해주세요.
def solution(n):
    answer = 0
    b = n // 2
    for x in range(1,b+1):
        answer += x * 2
    return answer

# 짝수를 더해야하므로 초기값은 0임에 유의

'''
#sol_1
def solution(n):
    return sum([i for i in range(2, n + 1, 2)])

#sol_2
def solution(n):
    return 2*(n//2)*((n//2)+1)/2
'''