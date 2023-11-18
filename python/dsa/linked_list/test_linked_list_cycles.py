# think of a solution
# 5 min - write code
# 3 min - verify correctness
class MyNode:
    def __init__(self, data, *args):
        self.data = data
        self.next = args[0] if args else None
        self.visited = 0

class MyLinkedList:
    def __init__(self):
        self.head = None

    def hasCycles(self) -> bool:
        node = self.head
        while node:
            node.visited = node.visited + 1
            if node.visited > 1: return True
            node = node.next
        return False

def test_1():
    linkedList = MyLinkedList()
    assert linkedList.hasCycles() == False

def test_2():
    linkedList = MyLinkedList()
    linkedList.next = MyNode('A')
    assert linkedList.hasCycles() == False

def test_3():
    linkedList = MyLinkedList()
    linkedList.head = MyNode('A')
    linkedList.head.next = linkedList.head
    assert linkedList.hasCycles() == True

def test_4():
    linkedList = MyLinkedList()
    linkedList.head = MyNode('A')
    linkedList.head.next = MyNode('B')
    linkedList.head.next.next = linkedList.head
    assert linkedList.hasCycles() == True
