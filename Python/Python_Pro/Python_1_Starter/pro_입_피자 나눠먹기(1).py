#https://school.programmers.co.kr/learn/courses/30/lessons/120814
#머쓱이네 피자가게는 피자를 일곱 조각으로 잘라 줍니다. 피자를 나눠먹을 사람의 수 n이 주어질 때, 모든 사람이 피자를 한 조각 이상 먹기 위해 필요한 피자의 수를 return 하는 solution 함수를 완성해보세요.
def solution(n):
    count = n // 7
    if n % 7 != 0 : return count+1 
    else : return count

'''
# sol1
def solution(n):
    return (n - 1) // 7 + 1

# sol2
def solution(n):
    return -(-n//7)

# sol3
import math

def solution(n):
    return math.ceil(n/7)
    '''