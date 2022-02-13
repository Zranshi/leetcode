# -*- coding: UTF-8 -*-
# @Time     : 2021/09/01 07:40
# @Author   : Ranshi
# @File     : 123.py
from type.listNode import ListNode


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        new_head = ListNode(next=None, val=0)
        cur, p1, p2 = new_head, l1, l2
        while p1 and p2:
            if p1.val <= p2.val:
                cur.next, p1 = p1, p1.next
            else:
                cur.next, p2 = p2, p2.next
            cur = cur.next
        if p1:
            cur.next = p1
        elif p2:
            cur.next = p2
        return new_head.next
