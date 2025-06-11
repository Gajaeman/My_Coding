class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class Stack:
    def __init__(self):
        self.top = None
    def push(self, data):
        newNode = Node(data)
        newNode.next = self.top
        self.top = newNode
    def pop(self):
        if self.top is None:
            print("스택 비었음")
        else:
            val = self.top.data
            self.top = self.top.next
            return val

    def whatTopis(self):
        if self.top is None:
            print("스택 비었음")
        else:
            return self.top.data

a = Stack()
a.push(10)
a.push(20)
a.push(30)
print(a.pop())
print(a.whatTopis())
print(a.pop())
print(a.pop())
print(a.pop())