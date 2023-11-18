#!/usr/local/bin/pytest
import unittest

# MyLinkedList class:
#       getAtIndex(idx: int) ->  int - get value at index, -1 if index is invalid
#            addAtHead(data) -> None - add at start
#            addAtTail(data) -> None - add at end
# addAtIndex(idx: int, data) -> None - add before index, add at end if index == len, dont add if index > len
#    deleteAtIndex(idx: int) -> None - delete at index, if index is valid

class MyNode:

    def __init__(self, data, *args):
        self.data = data
        self.next = args[0] if args else None

class MyLinkedList:

    def __init__(self):
        self.head = None

    def getAtIndex(self, idx: int) -> int:
        i = 0
        node = self.head
        while node and i < idx:
            node = node.next
            i = i + 1
        return node.data if node and idx >= 0 else -1

    def addAtHead(self, data) -> None:
        self.head = MyNode(data, self.head)

    def addAtTail(self, data) -> None:
        node = self.head
        while node and node.next:
            node = node.next
        newNode = MyNode(data)
        if node:
            node.next = newNode
        else:
            self.head = newNode

    def addAtIndex(self, idx: int, data) -> None:
        # add before index, add at end if index == len, dont add if index > len
        if idx < 0: return
        # dont add if idx == 0 and empty list
        elif idx == 0 and not self.head: return
        elif idx == 0 and self.head:
            self.head = MyNode(data, self.head)
            return
        elif idx > 0 and not self.head: return
        # idx > 0 and self.head is not null, i.e. list not empty
        i = 0
        node = self.head
        while node and i < idx - 1:
            node = node.next
            i = i + 1
        # node is not null
        # idx > 0 and i < idx - 1 for non empty list means that idx is out of bounds
        if i < idx - 1: return
        newNode = MyNode(data, node.next)
        node.next = newNode

    def deleteAtIndex(self, idx: int) -> None:
        if idx < 0: return
        elif idx == 0 and not self.head: return
        elif idx == 0 and self.head: self.head = self.head.next
        # idx > 0
        i = 0
        node = self.head
        while node and node.next and i < idx - 1:
            node = node.next
            i = i + 1
        if not node or not node.next or i < idx - 1: return
        node.next = node.next.next

class MyLinkedListTests(unittest.TestCase):

    def setUp(self):
        self.linkedList = MyLinkedList()

    def test_GET_AT_INDEX(self):
        self.linkedList.head = MyNode(1)
        self.assertEqual(self.linkedList.getAtIndex(0), 1)

    def test_GET_AT_INDEX_0_EMPTY(self):
        self.assertEqual(self.linkedList.getAtIndex(0), -1)

    def test_GET_AT_NEGATIVE_INDEX(self):
        self.assertEqual(self.linkedList.getAtIndex(-1), -1)

    def test_ADD_AT_HEAD_EMPTY(self):
        self.linkedList.addAtHead(1)
        self.assertEqual(self.linkedList.head.data, 1)
        self.assertEqual(self.linkedList.head.next, None)

    def test_ADD_AT_HEAD(self):
        self.linkedList.head = MyNode(2)
        self.linkedList.addAtHead(1)
        self.assertEqual(self.linkedList.head.data, 1)
        self.assertEqual(self.linkedList.head.next.data, 2)

    def test_ADD_AT_TAIL_EMPTY(self):
        self.linkedList.addAtTail(1)
        self.assertEqual(self.linkedList.head.data, 1)
        self.assertEqual(self.linkedList.head.next, None)

    def test_ADD_AT_TAIL(self):
        self.linkedList.head = MyNode(1)
        self.linkedList.addAtTail(2)
        self.assertEqual(self.linkedList.head.data, 1)
        self.assertEqual(self.linkedList.head.next.data, 2)

    def test_ADD_AT_INDEX_1(self):
        self.linkedList.head = MyNode(1)
        self.linkedList.addAtIndex(0, 2)
        self.assertEqual(self.linkedList.head.data, 2)
        self.assertEqual(self.linkedList.head.next.data, 1)
        self.assertEqual(self.linkedList.head.next.next, None)

    def test_ADD_AT_INDEX_2(self):
        self.linkedList.head = MyNode(1)
        self.linkedList.head.next = MyNode(2)
        self.linkedList.addAtIndex(1, 3)
        self.assertEqual(self.linkedList.head.data, 1)
        self.assertEqual(self.linkedList.head.next.data, 3)
        self.assertEqual(self.linkedList.head.next.next.data, 2)

    def test_ADD_AT_INDEX_1_EMPTY(self):
        self.linkedList.addAtIndex(0, 1)
        self.assertEqual(self.linkedList.head, None)

    def test_ADD_AT_NEGATIVE_INDEX(self):
        self.linkedList.addAtIndex(-1, 1)
        self.assertEqual(self.linkedList.head, None)

    def test_DELETE_AT_INDEX_0(self):
        self.linkedList.head = MyNode(1)
        self.linkedList.deleteAtIndex(0)
        self.assertEqual(self.linkedList.head, None)

    def test_DELETE_AT_INDEX_1_1(self):
        self.linkedList.head = MyNode(1)
        self.linkedList.head.next = MyNode(2)
        self.linkedList.deleteAtIndex(1)
        self.assertEqual(self.linkedList.head.data, 1)

    def test_DELETE_AT_INDEX_1_2(self):
        self.linkedList.head = MyNode(1)
        self.linkedList.head.next = MyNode(2)
        self.linkedList.head.next.next = MyNode(3)
        self.linkedList.deleteAtIndex(1)
        self.assertEqual(self.linkedList.head.data, 1)
        self.assertEqual(self.linkedList.head.next.data, 3)
        self.assertEqual(self.linkedList.head.next.next, None)
