#https://school.programmers.co.kr/learn/courses/30/lessons/120905
#정수 n과 정수 배열 numlist가 매개변수로 주어질 때, numlist에서 n의 배수가 아닌 수들을 제거한 배열을 return하도록 solution 함수를 완성해주세요.
def solution(n, numlist):
    L = []
    for x in numlist : 
        if x % n == 0 : L.append(x)
    return L


"""
# sol_1
def solution(n, numlist):
    return list(filter(lambda v: v%n==0, numlist))

# sol_2
def solution(n, numlist):
    return [i for i in numlist if i%n==0] 
"""