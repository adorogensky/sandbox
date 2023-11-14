#!/usr/bin/python3
import unittest
# how do we delete when an element if it was added more than one time
# tests and implementation from scratch took 1 hr (5 hr of sleep and emotional fatigue)
class MyLinkedList:

    def __init__(self):
        self._next = None
        self._last = None

    def contains(self, el):
        if self._next == None:
            return
        elif self._next == self._last:
            return self._next._value == el

        curNode = self._next

        while curNode != self._last:
            if curNode._value == el:
                return True
            curNode = curNode._next
        return False

    def add(self, el):
        newNode = MyLinkedList()
        newNode._value = el
        
        if self._next == None:
            self._next = newNode
            self._last = newNode
        else:
            self._last._next = newNode

    def remove(self, el):
        if self._last == None:
            return
        elif self._next == self._last and self._next._value == el:
            self._next = None
            self._last = None
            return

        curNode = self._next
        prevNode = None

        while curNode != self._last:
            if curNode._value == el:
                if prevNode == None:
                    self._next = curNode._next
                else:
                    prevNode._next = curNode._next


class MyLinkedListTests(unittest.TestCase):

    def test_new_list_contains(self):
        self.assertFalse(MyLinkedList().contains(1))

    def test_contains_after_add(self):
        l_list = MyLinkedList()
        l_list.add(1)
        self.assertTrue(l_list.contains(1))

    def test_contains_after_remove(self):
        l_list = MyLinkedList()
        l_list.add(1)
        l_list.remove(1)
        self.assertFalse(l_list.contains(1))

if __name__ == '__main__':
    unittest.main()
