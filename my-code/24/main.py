# -*- coding: UTF-8 -*-
# @Time     : 2021/08/16 17:23
# @Author   : Ranshi
# @File     : main.py


class ListNode:

    def __init__(self, val=0, next: 'ListNode' = None):
        self.val = val
        self.next = next


class Solution:

    def swapPairs(self, head: ListNode) -> ListNode:
        new_head = ListNode(val=0, next=head)
        cur = new_head
        while cur.next and cur.next.next:
            node1 = cur.next
            node2 = cur.next.next
            cur.next = node2
            node1.next = node2.next
            node2.next = node1
            cur = cur.next.next
        return new_head.next
