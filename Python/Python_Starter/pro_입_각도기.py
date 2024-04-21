#https://school.programmers.co.kr/learn/courses/30/lessons/120829
#각에서 0도 초과 90도 미만은 예각, 90도는 직각, 90도 초과 180도 미만은 둔각 180도는 평각으로 분류합니다. 각 angle이 매개변수로 주어질 때 예각일 때 1, 직각일 때 2, 둔각일 때 3, 평각일 때 4를 return하도록 solution 함수를 완성해주세요.
def solution(angle):
    if 0 < angle < 90:
        answer = '예각'
    elif angle == 90:
        answer = '직각'
    elif 90 < angle < 180:
        answer = '둔각'
    elif angle == 180:
        answer = '평각'
    else:
        answer = '기타'
    return answer
print(solution(180))

'''
#sol_1   ???
def solution(angle):
    answer = (angle // 90) * 2 + (angle % 90 > 0) * 1
    return answer

#sol_2
def solution(angle):
    if angle<=90:
        return 1 if angle<90 else 2
    else:
        return 3 if angle<180 else 4


'''