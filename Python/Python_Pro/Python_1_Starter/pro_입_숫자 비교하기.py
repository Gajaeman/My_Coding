#https://school.programmers.co.kr/learn/courses/30/lessons/120807
#정수 num1과 num2가 매개변수로 주어집니다. 두 수가 같으면 1 다르면 -1을 retrun하도록 solution 함수를 완성해주세요.
def solution(num1, num2):
    if num1 - num2 == 0 : answer = 1
    else : answer = -1
    return answer
print(solution(3,4))

'''
#sol_1
def solution(num1, num2):
    return 1 if num1==num2 else -1
'''