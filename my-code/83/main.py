# -*- coding:utf-8 -*-
# @Time     : 2021/05/28 17: 57
# @Author   : Ranshi
# @File     : 83. 删除排序链表中的重复元素.py
from type.listNode import ListNode


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        p = head
        while p.next:
            if p.next.val == p.val:
                p.next = p.next.next
            else:
                p = p.next
        return head
