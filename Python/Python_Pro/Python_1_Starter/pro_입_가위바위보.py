#https://school.programmers.co.kr/learn/courses/30/lessons/120839
#가위는 2 바위는 0 보는 5로 표현합니다. 가위 바위 보를 내는 순서대로 나타낸 문자열 rsp가 매개변수로 주어질 때, rsp에 저장된 가위 바위 보를 모두 이기는 경우를 순서대로 나타낸 문자열을 return하도록 solution 함수를 완성해보세요.
def solution(rsp):
    result = ''
    for char in rsp:
        if char == '2':  # 가위일 때
            result += '0'  # 바위로 이김
        elif char == '0':  # 바위일 때
            result += '5'  # 보로 이김
        elif char == '5':  # 보일 때
            result += '2'  # 가위로 이김
    return result


'''
# sol_1
def solution(rsp):
    d = {'0':'5','2':'0','5':'2'}
    return ''.join(d[i] for i in rsp)

# sol_2
def solution(rsp):
    rsp =rsp.replace('2','s')
    rsp =rsp.replace('5','p')
    rsp =rsp.replace('0','r')
    rsp =rsp.replace('r','5')
    rsp =rsp.replace('s','0')
    rsp =rsp.replace('p','2')
    return rsp

# sol_3
def solution(rsp):
    return rsp.translate(str.maketrans('025', '502'))
'''