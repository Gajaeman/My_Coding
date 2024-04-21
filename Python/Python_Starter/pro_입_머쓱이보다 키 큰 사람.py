#https://school.programmers.co.kr/learn/courses/30/lessons/120585
#머쓱이는 학교에서 키 순으로 줄을 설 때 몇 번째로 서야 하는지 궁금해졌습니다. 머쓱이네 반 친구들의 키가 담긴 정수 배열 array와 머쓱이의 키 height가 매개변수로 주어질 때, 머쓱이보다 키 큰 사람 수를 return 하도록 solution 함수를 완성해보세요.
def solution(array, height):
    count = 0
    for x in array : 
        if x > height :
            count += 1
    return count

"""
#sol_1
def solution(array, height):
    array.append(height)
    array.sort(reverse=True)
    return array.index(height)

-> 리스트에 추가하여 정렬 후 인덱스 번호 출력

#sol_2
def solution(array, height):
    return sum(1 for a in array if a > height)
"""