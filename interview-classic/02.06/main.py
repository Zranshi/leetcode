# -*- coding:utf-8 -*-
# @Time     : 2021/6/28 14: 23
# @Author   : Ranshi
# @File     : 面试题 02.06. 回文链表.py

from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, _next: Optional['ListNode'] = None):
        self.val = val
        self.next = _next


class Solution:

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return True

        # 找到前半部分链表的尾节点并反转后半部分链表
        first_half_end = self.end_of_first_half(head)
        if first_half_end:
            second_half_start = self.reverse_list(first_half_end.next)
        else:
            second_half_start = None
        # 判断是否回文
        result = True
        first_position = head
        second_position = second_half_start
        while result and second_position is not None:
            if first_position:
                if first_position.val != second_position.val:
                    result = False
                first_position = first_position.next
                second_position = second_position.next

        # 还原链表并返回结果
        if first_half_end and second_half_start:
            first_half_end.next = self.reverse_list(second_half_start)
        return result

    def end_of_first_half(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head
        while fast and fast.next and fast.next.next and slow:
            fast = fast.next.next
            slow = slow.next
        return slow

    def reverse_list(self, head: Optional[ListNode]):
        previous = None
        current = head
        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        return previous
