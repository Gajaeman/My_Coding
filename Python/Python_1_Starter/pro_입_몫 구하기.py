#https://school.programmers.co.kr/learn/courses/30/lessons/120804
#정수 num1, num2가 매개변수로 주어질 때, num1을 num2로 나눈 몫을 return 하도록 solution 함수를 완성해주세요.
def solution(num1, num2):
    answer = num1 // num2
    return answer

'''
#sol_1
solution = int.__floordiv__

-> 학습


#sol_2
def solution(num1, num2):
    answer = num1 / num2
    return int(answer)

-> 나누고 int 이용해서 소수점 날리기 가능


#sol_3
def solution(num1, num2):
    return divmod(num1, num2)[0]

    -> divmod는 몫과 나머지를 구할 수 있다. 
    [0]이 몫, [1]이 나머지

    
#sol_4
solution = lambda x, y : x//y
-> 람다 이용하여 간략화 (return은 왜 필요 없는지?)
'''