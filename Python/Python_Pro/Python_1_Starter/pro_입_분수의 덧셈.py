#https://school.programmers.co.kr/learn/courses/30/lessons/120808
#첫 번째 분수의 분자와 분모를 뜻하는 numer1, denom1, 두 번째 분수의 분자와 분모를 뜻하는 numer2, denom2가 매개변수로 주어집니다. 두 분수를 더한 값을 기약 분수로 나타냈을 때 분자와 분모를 순서대로 담은 배열을 return 하도록 solution 함수를 완성해보세요.
import math

def solution(numer1, denom1, numer2, denom2):
    common_denom = denom1 * denom2
    new_numer = numer1 * denom2 + numer2 * denom1
    
    gcd_value = math.gcd(new_numer, common_denom)
    
    new_numer //= gcd_value
    common_denom //= gcd_value
    
    return [new_numer, common_denom]

""" # 모듈 없이 계산
def solution(denum1, num1, denum2, num2):
    answer = []
    s = 0

    denum0 = (denum1*num2) +(denum2*num1)
    num0 = num1*num2

    for i in range(min(denum0,num0),0,-1):
        if denum0%i == 0 and num0%i == 0:
            s = i
            break

    denum0 /= s
    num0 /= s
    answer.append(denum0)
    answer.append(num0)

    return answer
"""