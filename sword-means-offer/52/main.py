# -*- coding: UTF-8 -*-
# @Time     : 2021/10/03 22:06
# @Author   : Ranshi
# @File     : main.py
from type.list_node import ListNode


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        node1, node2 = headA, headB

        while node1 != node2:
            node1 = node1.next if node1 else headB
            node2 = node2.next if node2 else headA

        return node1
