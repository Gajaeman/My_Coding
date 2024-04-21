#https://school.programmers.co.kr/learn/courses/30/lessons/120826
#문자열 my_string과 문자 letter이 매개변수로 주어집니다. my_string에서 letter를 제거한 문자열을 return하도록 solution 함수를 완성해주세요.
def solution(my_string, letter):
    return my_string.replace(letter, "")

'''
#sol_1
def solution(my_string, letter):
    answer = ''
    for string in my_string:
        if string != letter:
            answer += string
    return answer

#sol_2
def solution(my_string, letter):
    return ''.join([c for c in my_string if c != letter])
'''