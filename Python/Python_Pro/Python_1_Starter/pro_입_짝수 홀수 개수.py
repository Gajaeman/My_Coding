#https://school.programmers.co.kr/learn/courses/30/lessons/120824
#정수가 담긴 리스트 num_list가 주어질 때, num_list의 원소 중 짝수와 홀수의 개수를 담은 배열을 return 하도록 solution 함수를 완성해보세요.
def solution(num_list):
    a, b = 0, 0
    for x in num_list : 
        if int(x) % 2 == 0 : a += 1
        else : b += 1
    return [a, b]

"""
#sol_1
def solution(num_list):
    answer = [0,0]
    for n in num_list:
        answer[n%2]+=1
    return answer


#sol_2
def solution(num_list):
    odd = sum(1 for n in num_list if n % 2)
    return [len(num_list) - odd, odd]
"""