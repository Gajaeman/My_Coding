#https://school.programmers.co.kr/learn/courses/30/lessons/120825
#문자열 my_string과 정수 n이 매개변수로 주어질 때, my_string에 들어있는 각 문자를 n만큼 반복한 문자열을 return 하도록 solution 함수를 완성해보세요.
def solution(my_string, n):
    string = ''
    for x in my_string : 
        string += x*n
    return string

"""
# sol_1
def solution(my_string, n):
    return ''.join(i*n for i in my_string)

# sol_2 리스트 왜쓴거지?
def solution(my_string, n):
    answer = ''

    for c in list(my_string):
        answer += c*n
    return answer
"""