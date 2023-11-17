#!/usr/bin/python3
import unittest

class MyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None
    
    def addAtHead(self, data):
        newNode = MyLinkedListNode(data)
        newNode.next = self.head
        self.head = newNode

    def addAtTail(self, data):
        node = self.head
        while node and node.next:
            node = node.next
        newNode = MyLinkedListNode(data)
        if node:
            node.next = newNode
        else:
            self.head = newNode

    def addAtIndex(self, idx: int, data):
        i = 0
        node = self.head
        while node and i < idx - 1: 
            node = node.next
        if not node:
            raise Exception(f'index {idx} is out of bounds')
        newNode = MyLinkedListNode(data)
        if idx > 0:
            newNode.next = node.next
            node.next = newNode
        else:
            newNode.next = node
            self.head = newNode

    def getAtIndex(self, idx: int):
        i = 0
        node = self.head
        while node and i < idx:
            node = node.next
        if not node or idx < 0:
            raise Exception(f'index {idx} is out of bounds')
        return node.data

    def deleteAtIndex(self, idx: int):
        i = 0
        node = self.head
        while node and i < idx - 1:
            node = node.next
            i = i + 1
        if not node or idx < 0:
            raise Exception(f'index {idx} is out of bounds')
        if idx > 0:
            node.next = node.next.next if node.next else None 
        else:
            self.head = node.next.next if node.next else None

class MyLinkedListTests(unittest.TestCase):
    
    def setUp(self):
        self.linkedList = MyLinkedList()

    def test_ADD_AT_HEAD_EMPTY_LIST(self):
        self.linkedList.addAtHead(1)
        self.assertEqual(self.linkedList.head.data, 1)
        self.assertEqual(self.linkedList.head.next, None)

    def test_ADD_AT_HEAD_EMPTY(self):
        self.linkedList.head = MyLinkedListNode(2)
        self.linkedList.addAtHead(1)
        self.assertEqual(self.linkedList.head.data, 1)
        self.assertEqual(self.linkedList.head.next.data, 2)

    def test_ADD_AT_TAIL_EMPTY_LIST(self):
        self.linkedList.addAtTail(1)
        self.assertEqual(self.linkedList.head.data, 1)
        self.assertEqual(self.linkedList.head.next, None)

    def test_ADD_AT_TAIL(self):
        self.linkedList.head = MyLinkedListNode(1)
        self.linkedList.addAtTail(2)
        self.assertEqual(self.linkedList.head.data, 1)
        self.assertEqual(self.linkedList.head.next.data, 2)

    def test_ADD_AT_INDEX_1(self):
        self.linkedList.head = MyLinkedListNode(1)
        self.linkedList.addAtIndex(0, 2)
        self.assertEqual(self.linkedList.head.data, 2)
        self.assertEqual(self.linkedList.head.next.data, 1)
        self.assertEqual(self.linkedList.head.next.next, None)

    def test_ADD_AT_INDEX_2(self):
        self.linkedList.head = MyLinkedListNode(1)
        self.linkedList.head.next = MyLinkedListNode(2)
        self.linkedList.addAtIndex(1, 3)
        self.assertEqual(self.linkedList.head.data, 1)
        self.assertEqual(self.linkedList.head.next.data, 3)
        self.assertEqual(self.linkedList.head.next.next.data, 2)

    def test_ADD_AT_INDEX_EMPTY_LIST(self):
        with self.assertRaises(Exception) as ctx:
            self.linkedList.addAtIndex(0, 1)
        self.assertTrue('index 0 is out of bounds' in str(ctx.exception))

    def test_ADD_AT_NEGATIVE_INDEX(self):
        with self.assertRaises(Exception) as ctx:
            self.linkedList.addAtIndex(-1, 1)
        self.assertTrue('index -1 is out of bounds' in str(ctx.exception))
        self.assertEqual(self.linkedList.head, None)

    def test_GET_AT_INDEX(self):
        self.linkedList.head = MyLinkedListNode(1)
        self.assertEqual(self.linkedList.getAtIndex(0), 1)

    def test_GET_AT_INDEX_EMPTY_LIST(self):
        with self.assertRaises(Exception) as ctx:
            self.linkedList.getAtIndex(0)
        self.assertTrue('index 0 is out of bounds' in str(ctx.exception))

    def test_GET_AT_NEGATIVE_INDEX(self):
        with self.assertRaises(Exception) as ctx:
            self.linkedList.getAtIndex(-1)
        self.assertTrue('index -1 is out of bounds' in str(ctx.exception))

    def test_DELETE_AT_INDEX_0(self):
        self.linkedList.head = MyLinkedListNode(1)
        self.linkedList.deleteAtIndex(0)
        self.assertEqual(self.linkedList.head, None)

    def test_DELETE_AT_INDEX_1_1(self):
        self.linkedList.head = MyLinkedListNode(1)
        self.linkedList.head.next = MyLinkedListNode(2)
        self.linkedList.deleteAtIndex(1)
        self.assertEqual(self.linkedList.head.data, 1)

    def test_DELETE_AT_INDEX_1_2(self):
        self.linkedList.head = MyLinkedListNode(1)
        self.linkedList.head.next = MyLinkedListNode(2)
        self.linkedList.head.next.next = MyLinkedListNode(3)
        self.linkedList.deleteAtIndex(1)
        self.assertEqual(self.linkedList.head.data, 1)
        self.assertEqual(self.linkedList.head.next.data, 3)
        self.assertEqual(self.linkedList.head.next.next, None)


if __name__ == '__main__':
    unittest.main()
