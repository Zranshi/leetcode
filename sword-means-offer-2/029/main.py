# -*- coding: UTF-8 -*-
# @Time     : 2022/01/20 23:07
# @Author   : Ranshi
# @File     : 123.py
# @Doc      : 剑指 Offer II 029. 排序的循环链表
from pyal.container import ListNode as Node


class Solution:
    def insert(self, head: "Node", insertVal: int) -> "Node":
        if not head:
            node = Node(val=insertVal)
            node.next = node
            return node
        pre, node = head, Node(val=insertVal)
        while True:
            if (
                pre.val <= insertVal <= pre.next.val
                or (pre.next.val < pre.val and (insertVal >= pre.val or insertVal <= pre.next.val))
                or pre.next == head
            ):
                pre.next, node.next = node, pre.next
                break
            pre = pre.next
        return head
