# -*- coding:utf-8 -*-
# @Time     : 2021/6/28 21: 02
# @Author   : Ranshi
# @File     : 面试题 02.08. 环路检测.py
from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, _next: Optional['ListNode'] = None):
        self.val = val
        self.next = _next


class Solution:
    def detectCycle(self, head: ListNode) -> Optional[ListNode]:
        slow, fast = head, head
        while fast and fast.next and slow:  # 开始走位
            slow = slow.next
            fast = fast.next.next
            if slow == fast:  # 相遇
                break

        # 若无相会处，则无环路
        if not fast or not fast.next:
            return None
        # 若两者以相同的速度移动，则必然在环路起始处相遇
        slow = head
        while slow != fast and slow and fast:
            slow = slow.next
            fast = fast.next
        return slow
