#https://school.programmers.co.kr/learn/courses/30/lessons/120806
#정수 num1과 num2가 매개변수로 주어질 때, num1을 num2로 나눈 값에 1,000을 곱한 후 정수 부분을 return 하도록 soltuion 함수를 완성해주세요.
def solution(num1, num2):
    a = (num1 / num2)*1000
    answer = int(a)
    return answer

'''
#sol_1
def solution(num1, num2):
    return int(num1 / num2 * 1000)

#sol_2
def solution(num1, num2):
    answer = (num1/num2)*1000
    return answer//1

-> // 1 을 이용해 몫만 추출할 수 있음 
'''