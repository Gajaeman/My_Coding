#https://school.programmers.co.kr/learn/courses/30/lessons/120804
#정수 num1, num2가 매개변수 주어집니다. num1과 num2를 곱한 값을 return 하도록 solution 함수를 완성해주세요.
def solution(num1, num2):
    answer = num1 * num2
    return answer

'''
#sol_1
def solution(num1, num2):
    #return num1 * num2
    i = 0
    answer = 0
    while i < num2:
        answer += num1
        i += 1
    return answer

-> num1을 num2번 더해주는 방식


#sol_2
def solution(*num1):
    return num1[0]*num1[1]

-> 학습
'''
