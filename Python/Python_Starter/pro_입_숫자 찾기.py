#https://school.programmers.co.kr/learn/courses/30/lessons/120904?language=python3
#정수 num과 k가 매개변수로 주어질 때, num을 이루는 숫자 중에 k가 있으면 num의 그 숫자가 있는 자리 수를 return하고 없으면 -1을 return 하도록 solution 함수를 완성해보세요.
def solution(num, k):
    sin = len(str(num))
    answer, c = -1 , 1
    for p in range(sin-1, -1, -1) :
        a = num // 10**p
        num %= 10**p
        if a == k :
            answer = sin - p
            return answer
    return answer


'''
#sol_1
def solution(num, k):
    str_num, str_k = str(num), str(k)
    if str_k in str_num:
        return (str_num.index(str_k)+1)
    else:
        return -1

print(solution(1234, 4))
'''