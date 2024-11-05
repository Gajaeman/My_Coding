#https://school.programmers.co.kr/learn/courses/30/lessons/120813?language=python3
#정수 n이 매개변수로 주어질 때, n 이하의 홀수가 오름차순으로 담긴 배열을 return하도록 solution 함수를 완성해주세요.
def solution(n):
    answer =[]
    for x in range(1, n+1, 2):
        answer.append(x)
    return answer

""" 컴프리핸션
def solution(n):
    return [i for i in range(1, n+1, 2)]
"""