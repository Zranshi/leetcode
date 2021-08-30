# -*- coding:utf-8 -*-
# @Time     : 2021/07/29 00:53
# @Author   : Ranshi
# @File     : main.py

from typing import Optional


class ListNode:

    def __init__(self, val: int = 0, _next: Optional['ListNode'] = None):
        self.val = val
        self.next = _next


class Solution:

    def middleNode(self, head: ListNode) -> Optional[ListNode]:
        slow, fast = head, head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
