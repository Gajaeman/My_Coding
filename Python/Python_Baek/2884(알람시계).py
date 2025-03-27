h,m = map(int, input().split())
if m<45 and h==0 : print(23, m+15)
elif m<45 : print(h-1, m+15)
else : print(h, m-45)

#print((h-1) % 24 if m < 45 else h, (m+15) % 60)
#=> 나머지 이용하여 간락히 계산 가능