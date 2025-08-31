n, m = map(int, input().split()) # N:노드 개수, M:거리 알고싶은 노드 쌍 개수
E = n-1
dis = 0
for _ in range(n-1):
    Data = list(map(int, input().split())) #두 점, 두 점 사이의 거리
for k in range(len(Data)//3):
    start = []

for _ in range(m):
    from_, to_ = map(int, input().split()) # 거리 알고싶은 노드 쌍




Tree = [[0] * 5 for _ in range(n+1)]		
for i in range(n+1) :		
    Tree[i][3] = Tree[i][4] = -1		
Tree[1][4] = 0		
		
for i in range(E):		
    parent, child = Data[i*3:i*3+2] # 슬라이싱 대입		
    if Tree[parent][0] == 0: # lc가 없으면		
        Tree[parent][0] = child		
    else : Tree[parent][1] = child		
    Tree[parent][2] += 1  # degree		
    Tree[child][3] = parent  # parent		
    Tree[child][4] = Tree[parent][4] + 1  # lenel		
for i in range(n+1): print(Tree[i])		
