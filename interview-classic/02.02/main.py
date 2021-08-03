# -*- coding:utf-8 -*-
# @Time     : 2021/6/27 22: 33
# @Author   : Ranshi
# @File     : 面试题 02.02. 返回倒数第 k 个节点.py
from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, _next: Optional['ListNode'] = None):
        self.val = val
        self.next = _next


class Solution:
    def kthToLast(self, head: Optional[ListNode], k: int) -> int:
        cur = pre = head
        for _ in range(k):
            if cur:
                cur = cur.next
        while cur and pre:
            cur, pre = cur.next, pre.next
        if pre:
            return pre.val
        return -1
