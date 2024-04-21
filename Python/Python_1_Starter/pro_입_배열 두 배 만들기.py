#https://school.programmers.co.kr/learn/courses/30/lessons/120809
#정수 배열 numbers가 매개변수로 주어집니다. numbers의 각 원소에 두배한 원소를 가진 배열을 return하도록 solution 함수를 완성해주세요.
def solution(numbers):
    answer = [num * 2 for num in numbers]
    return answer

"""
-> 리스트 자체로는 연산 불가능하므로 새로운 리스트 생성

#sol_1
def solution(numbers):
    return list(map(lambda x: x * 2, numbers))
"""