# -*- coding:utf-8 -*-
# @Time     : 2021/6/27 22: 22
# @Author   : Ranshi
# @File     : 面试题 02.01. 移除重复节点.py
from typing import Set, Optional


class ListNode:
    def __init__(self, val: int = 0, _next: Optional["ListNode"] = None):
        self.val = val
        self.next = _next


class Solution:
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        cur = head
        c: Set[int] = set()
        c.add(head.val)
        while cur.next is not None:
            if cur.next.val not in c:
                c.add(cur.next.val)
                cur = cur.next
            else:
                cur.next = cur.next.next
        return head
