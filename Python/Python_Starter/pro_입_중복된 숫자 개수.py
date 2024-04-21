#https://school.programmers.co.kr/learn/courses/30/lessons/120583
#정수가 담긴 배열 array와 정수 n이 매개변수로 주어질 때, array에 n이 몇 개 있는 지를 return 하도록 solution 함수를 완성해보세요.
def solution(array, n):
    count = 0
    for num in array:
        if num == n:
            count += 1
    return count

"""
#sol_1
def solution(array, n):
    return array.count(n)

#sol_2
def solution(array, n):
    return sum(1 for x in array if x == n)    
"""