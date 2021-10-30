# -*- coding:utf-8 -*-
# @Time     : 2021/6/28 20: 54
# @Author   : Ranshi
# @File     : 面试题 02.07. 链表相交.py
from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, _next: Optional["ListNode"] = None):
        self.val = val
        self.next = _next


class Solution:
    def getIntersectionNode(self, head_a: ListNode, head_b: ListNode) -> Optional[ListNode]:
        a, b = head_a, head_b
        while a != b:
            if not a:
                a = head_b
            else:
                a = a.next
            if not b:
                b = head_a
            else:
                b = b.next
        return a
