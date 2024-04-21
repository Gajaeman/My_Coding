#https://school.programmers.co.kr/learn/courses/30/lessons/120820
#머쓱이는 40살인 선생님이 몇 년도에 태어났는지 궁금해졌습니다. 나이 age가 주어질 때, 2022년을 기준 출생 연도를 return 하는 solution 함수를 완성해주세요.

def solution(age):
    answer = 2023 - age
    return answer

'''
#sol_1
def solution(age):
    return 2023-age

-> return에 바로 값 대입하여 한 줄 줄일 수 있음

#sol_2
def solution(age):
    import datetime
    return datetime.datetime.utcnow().year - age + 1

-> 학습
'''