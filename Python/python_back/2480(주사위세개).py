a, b, c = map(int, input().split())
if a==b==c : print(10000+a*1000)
elif a==b or b==c : print(1000+b*100)
elif a==c : print(1000+a*100)
else : print(max(a,b,c)*100)

''' 리스트와 집합을 이용한 풀이
a, b, c = map(int, input().split())
nums = [a, b, c]
uniq = set(nums)

if len(uniq) == 1:  # 세 숫자가 모두 같음
    print(10000 + a * 1000)
elif len(uniq) == 2:  # 두 개의 숫자가 같음
    for n in uniq:
        if nums.count(n) == 2:
            print(1000 + n * 100)
            break
else:  # 모든 숫자가 다름
    print(max(nums) * 100)
'''