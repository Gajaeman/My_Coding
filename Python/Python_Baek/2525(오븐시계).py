h,m = map(int, input().split())
t = int(input())
print((h+t//60)%24, (m+t%60)%60) if m+t%60<60 else print((1+h+t//60)%24, (m+t%60)%60)