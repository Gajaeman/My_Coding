#https://school.programmers.co.kr/learn/courses/30/lessons/120909
#어떤 자연수를 제곱했을 때 나오는 정수를 제곱수라고 합니다. 정수 n이 매개변수로 주어질 때, n이 제곱수라면 1을 아니라면 2를 return하도록 solution 함수를 완성해주세요.
def solution(n):
    count = 2
    for x in range(1, n):
        if n / x == x : 
            count = 1
            break
    return count

'''
# sol_1
def solution(n):
    return 1 if (n ** 0.5).is_integer() else 2

# sol_2
def solution(n):
    if n**(1/2) == int(n**(1/2)) :
        return 1
    else :
        return 2

# sol_3
def solution(n):
    if n**(1/2) == int(n**(1/2)) :
        return 1
    else :
        return 2
'''