import sys
sys.stdin = open("13_BinaryTree.txt", 'r')

def preTraversal(T):
    if T :
        print("%d" %T, end = ' ')
        preTraversal(Tree[T][0])
        preTraversal(Tree[T][1])

def inTraversal(T):
    if T:
        inTraversal(Tree[T][0])
        print("%d" %T, end = ' ')
        inTraversal(Tree[T][1])

def postTraversal(T):
    if T:
        postTraversal(Tree[T][0])
        postTraversal(Tree[T][1])
        print("%d" %T, end=' ')

def levelTraversal(T):
    queue = [T]
    while queue:
        T = queue.pop(0)
        print("%d" % T, end=' ')
        queue += [child for child in Tree[T][:2] if child]

V, E = map(int, input().split())
Data = list(map(int, input().split()))

Tree = [[0] * 5 for _ in range(V+1)]
for i in range(V+1) :
    Tree[i][3] = Tree[i][4] = -1
Tree[1][4] = 0

for i in range(E):
    parent, child = Data[i*2:i*2+2] # 슬라이싱 대입
    if Tree[parent][0] == 0: # lc가 없으면
        Tree[parent][0] = child
    else : Tree[parent][1] = child
    Tree[parent][2] += 1  # degree
    Tree[child][3] = parent  # parent
    Tree[child][4] = Tree[parent][4] + 1  # level
for i in range(V+1): print(Tree[i])

preTraversal(1)
print()
inTraversal(1)
print()
postTraversal(1)
print()
levelTraversal(1)