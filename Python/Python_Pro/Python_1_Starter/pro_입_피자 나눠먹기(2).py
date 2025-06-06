#https://school.programmers.co.kr/learn/courses/30/lessons/120815
#머쓱이네 피자가게는 피자를 여섯 조각으로 잘라 줍니다. 피자를 나눠먹을 사람의 수 n이 매개변수로 주어질 때, n명이 주문한 피자를 남기지 않고 모두 같은 수의 피자 조각을 먹어야 한다면 최소 몇 판을 시켜야 하는지를 return 하도록 solution 함수를 완성해보세요.
import math

def solution(n) : # 버전에 따라 lcm 사용 불가
    return n*6 // math.gcd(n,6) // 6

"""
# sol_1
def solution(n):
    i=1
    while(1):
        if (6*i)%n==0:
            return i
        i+=1

# sol_2
def solution(n):
    answer = 1
    while 6 * answer % n:
        answer += 1
    return answer
"""