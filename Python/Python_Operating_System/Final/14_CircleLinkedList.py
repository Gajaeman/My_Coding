class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
head  = None
tail = None

def addPerson(who):
    global head, tail
    newNode = Node(who)
    if not head :
        head = newNode
        tail = newNode
    else :
        tail.next = newNode
        tail = newNode

def thirdWillDie(pre):# Camel 기법(의미있는 단어의 시작 대문자 표기 -> 가독성 향상)
    pre = pre.next
    pre.next = pre.next.next
    return pre.next

for who in range(1, 42):
    addPerson(who)

tail.next = head
pre = head

while pre.next.next != pre:
    pre = thirdWillDie(pre)
print(pre.data)
print(pre.next.data)