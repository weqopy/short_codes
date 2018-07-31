"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param head: The first node of linked list.
    @return: The head of linked list.
    """

    def insertionSortList(self, head):
        first = ListNode(0)

        while head:
            tmp = first
            next = head.next
            while tmp.next and tmp.next.val < head.val:
                tmp = tmp.next
            head.next = tmp.next
            tmp.next = head
            head = next
        return first.next
