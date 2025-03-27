#https://school.programmers.co.kr/learn/courses/30/lessons/120854
#문자열 배열 strlist가 매개변수로 주어집니다. strlist 각 원소의 길이를 담은 배열을 retrun하도록 solution 함수를 완성해주세요.
def solution(strlist):
    answer = []
    for string in strlist:
        answer.append(len(string))
    return answer

"""
#sol_1
def solution(strlist):
    answer = list(map(len, strlist))
    return answer

#sol_2
def solution(strlist):
    return [len(str) for str in strlist]
"""