#https://school.programmers.co.kr/learn/courses/30/lessons/120812
#최빈값은 주어진 값 중에서 가장 자주 나오는 값을 의미합니다. 정수 배열 array가 매개변수로 주어질 때, 최빈값을 return 하도록 solution 함수를 완성해보세요. 최빈값이 여러 개면 -1을 return 합니다.

def solution(array):
    count_dict = {}
    
    for x in array: 
        if x in count_dict:
            count_dict[x] += 1
        else:
            count_dict[x] = 1

    max_count = max(count_dict.values())
    modes = [key for key, value in count_dict.items() if value == max_count]

    if len(modes) > 1:
        return -1
    else:
        return modes[0]

""" 뭔소리고
def solution(array):
    while len(array) != 0:
        for i, a in enumerate(set(array)):
            array.remove(a)
        if i == 0: return a
    return -1
"""