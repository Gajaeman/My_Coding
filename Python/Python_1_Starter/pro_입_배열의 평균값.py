#https://school.programmers.co.kr/learn/courses/30/lessons/120817
#정수 배열 numbers가 매개변수로 주어집니다. numbers의 원소의 평균값을 return하도록 solution 함수를 완성해주세요.
def solution(numbers):
    average = sum(numbers) / len(numbers)
    return average


"""
#sol_1 
import numpy as np
def solution(numbers):
    return np.mean(numbers)

-> 질문

#sol_2
def solution(numbers):
    return sum(numbers) / len(numbers)
"""