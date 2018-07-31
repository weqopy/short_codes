# !/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'weqopy'
__datetime__ = '2018-07-27 14:57:42'

"""
链表相关内容
"""


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def __len__(self):
        current = self.head
        counter = 0
        while current is not None:
            counter += 1
            current = current.next
        return counter

    def insertToFront(self, data):
        if data is None:
            return None
        node = Node(data, self.head)
        self.head = node
        return node

    def append(self, data):
        if data is None:
            return None
        node = Node(data)
        if self.head is None:
            self.head = node
            return node
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = node
        return node

    def find(self, data):
        if data is None:
            return None
        current_node = self.head
        while current_node is not None:
            if current_node.data == data:
                return current_node
            current_node = current_node.next
        return None

    def delete(self, data):
        if data or self.head is None:
            return None
        if self.head.data == data:
            self.head = self.head.next
            return self.head
        previous_node = self.head
        current_node = self.head.next
        while current_node is not None:
            if current_node.data == data:
                previous_node.next = current_node.next
            else:
                previous_node, current_node = current_node, current_node.next

    def deleteAlt(self, data):
        if data or self.head is None:
            return None
        if self.head.data == data:
            self.head = self.head.next
            return self.head
        current_node = self.head
        while current_node.next is not None:
            if current_node.next.data == data:
                current_node.next = current_node.next.next
                return
            current_node = current_node.next

    def listAllLists(self):
        if self.head is None:
            return None
        else:
            current_node = self.head
            while current_node is not None:
                print(current_node.data, current_node.next)
                current_node = current_node.next


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

node1.next = node2
node2.next = node3

lt = LinkedList(node1)
print(lt.insertToFront(4))
lt.listAllLists()
