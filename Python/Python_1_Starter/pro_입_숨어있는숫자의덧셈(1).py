#https://school.programmers.co.kr/learn/courses/30/lessons/120851
#문자열 my_string이 매개변수로 주어집니다. my_string안의 모든 자연수들의 합을 return하도록 solution 함수를 완성해주세요.
def solution(my_string):
    total = 0
    for x in my_string:
        if x.isdigit():  
            total += int(x)
    return total

"""
# sol_1
def solution(my_string):
    return sum(int(i) for i in my_string if i.isdigit())

# sol_2
def solution(my_string):
    answer = 0
    for i in my_string:
        try:
            answer = answer + int(i)
        except:
            pass
    return answer
    
    """