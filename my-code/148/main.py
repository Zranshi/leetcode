# -*- coding:utf-8 -*-
# @Time     : 2021/7/4 17: 14
# @Author   : Ranshi
# @File     : main.py
class ListNode:

    def __init__(self, val=0, _next=None):
        self.val = val
        self.next = _next


class Solution:

    def sortList(self, head: ListNode) -> ListNode:

        def sort_func(h: ListNode, tail: ListNode) -> ListNode:
            if not h:
                return h
            if h.next == tail:
                h.next = None
                return h
            slow = fast = h
            while fast != tail:
                slow = slow.next
                fast = fast.next
                if fast != tail:
                    fast = fast.next
            mid = slow
            return merge(sort_func(h, mid), sort_func(mid, tail))

        def merge(head1: ListNode, head2: ListNode) -> ListNode:
            dummy_head = ListNode(0)
            t, t1, t2 = dummy_head, head1, head2
            while t1 and t2:
                if t1.val <= t2.val:
                    t.next = t1
                    t1 = t1.next
                else:
                    t.next = t2
                    t2 = t2.next
                t = t.next
            if t1:
                t.next = t1
            elif t2:
                t.next = t2
            return dummy_head.next

        return sort_func(head, None)
