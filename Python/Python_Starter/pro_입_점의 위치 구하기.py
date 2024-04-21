#https://school.programmers.co.kr/learn/courses/30/lessons/120841
'''
def solution(dot):
    if dot[0] > 0 :
        if dot[1] > 0 : answer = 1
        else : answer = 4
    else :
        if dot[1] > 0 : answer = 2
        else : answer = 3
    return answer
'''

#sol_1
def solution(dot):
    quad = [(3,2),(4,1)]
    return quad[dot[0] > 0][dot[1] > 0]
print(solution([1,1]))
'''
#sol_2
def solution(dot):
    a, b = 1, 0
    if dot[0]*dot[1] > 0:
        b = 1
    if dot[1] < 0:
        a = 2
    return 2*a-b
->> 질문
'''