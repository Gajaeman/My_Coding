#https://school.programmers.co.kr/learn/courses/30/lessons/120821
#정수가 들어 있는 배열 num_list가 매개변수로 주어집니다. num_list의 원소의 순서를 거꾸로 뒤집은 배열을 return하도록 solution 함수를 완성해주세요.
def solution(num_list):
    answer = num_list[::-1]
    return answer

"""
#sol_1
def solution(num_list):
    num_list.reverse()
    return num_list
-> reverse 메소드로 표현 가능
"""