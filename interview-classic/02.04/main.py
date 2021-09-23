# -*- coding:utf-8 -*-
# @Time     : 2021/6/28 13: 13
# @Author   : Ranshi
# @File     : 面试题 02.04. 分割链表.py
from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, _next: Optional["ListNode"] = None):
        self.val = val
        self.next = _next


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head:
            return head
        cur = idx = head
        while cur:
            if cur.val < x and idx:
                cur.val, idx.val = idx.val, cur.val
                cur, idx = cur.next, idx.next
            else:
                cur = cur.next
        return head
