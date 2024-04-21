#https://school.programmers.co.kr/learn/courses/30/lessons/120847
#정수 배열 numbers가 매개변수로 주어집니다. numbers의 원소 중 두 개를 곱해 만들 수 있는 최댓값을 return하도록 solution 함수를 완성해주세요.
def solution(numbers):
    numbers.sort(reverse = True)
    return numbers[0] * numbers[1]

"""
내림차순 정렬 -> numbers.sort(reverse = True)

#sol_1
def solution(numbers):
    num1 = 0
    num2 = 0
    answer = 0

    numbers.sort()

    num1 = numbers.pop()
    num2 = numbers.pop()
    answer = num1 * num2

    return answer

->  pop을 통해 변수 입력
"""