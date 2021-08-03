# -*- coding:utf-8 -*-
# @Time     : 2021/6/28 14: 00
# @Author   : Ranshi
# @File     : 面试题 02.05. 链表求和.py
from typing import Optional


class ListNode:
    def __init__(self, x: int, _next: Optional['ListNode'] = None):
        self.val = x
        self.next = _next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(-1)
        p = head
        carry = 0
        while l1 or l2 or carry:
            n = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            carry = n // 10
            p.next = ListNode(n % 10)
            p = p.next
            l1, l2 = l1.next if l1 else None, l2.next if l2 else None
        return head.next
