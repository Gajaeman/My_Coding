class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def insertNode(whatnext, data):
    global head
    newNode = Node('구조')
    pre = head
    while pre.data != whatnext:
        pre = pre.next
    newNode.next = pre.next
    pre.next = newNode

def deleteNode(what):
    global head
    pre = head
    while pre.next.data != what:
        pre = pre.next
    pre.next = pre.next.next

node1 = Node(10)
node2 = Node(20)
node3 = Node('자료')
node4 = Node(40)
node5 = Node(50)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
head = node1

insertNode('자료', '구조')
deleteNode('자료')
p = node1
while p:
    print(p.data)
    p = p.next