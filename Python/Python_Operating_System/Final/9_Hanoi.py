def Hanoi(n, _from, _to, _spare):
    if n > 0:
        Hanoi(n-1, _from, _spare, _to)
        print('%d번 원반을 %s에서 %s로 옮김' %(n, _from, _to))
        Hanoi(n-1, _spare, _to, _from)

n = 3
Hanoi(n=3, _from = 'from',_to = 'to',_spare = 'spare')