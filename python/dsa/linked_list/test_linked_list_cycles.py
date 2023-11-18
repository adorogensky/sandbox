# think of a solution
# 5 min - write code
# 3 min - verify correctness
import sys
class MyNode:
    def __init__(self, data, *args):
        self.data = data
        self.next = args[0] if args else None
        self.visited = False

class MyLinkedList:
    def __init__(self):
        self.head = None

    def _hasCycles(self) -> bool:
        node = self.head
        while node:
            if node.visited: return True
            else: node.visited = True
            node = node.next
        return False

    def hasCycles(self) -> bool:
        ptr1 = self.head
        ptr2 = self.head
        itr1 = True
    
        while ptr1:
            if ptr1 == ptr2 and not itr1: return True
            itr1 = False
            ptr1 = ptr1.next
            ptr2 = ptr2.next.next if ptr2.next else False
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
