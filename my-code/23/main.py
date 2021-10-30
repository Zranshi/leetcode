# -*- coding: UTF-8 -*-
# @Time     : 2021/08/21 21:24
# @Author   : Ranshi
# @File     : main.py
from typing import List

from pyal.container import ListNode


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        res = None  # 设置初始结果为空
        for listi in lists:  # 逐个遍历 两两合并
            res = self.mergeTwoLists(res, listi)
        return res

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)  # 构造虚节点
        move = dummy  # 设置移动节点等于虚节点
        while l1 and l2:  # 都不空时
            if l1.val < l2.val:
                move.next = l1  # 移动节点指向数小的链表
                l1 = l1.next
            else:
                move.next = l2
                l2 = l2.next
            move = move.next
        move.next = l1 if l1 else l2  # 连接后续非空链表
        return dummy.next  # 虚节点仍在开头


if __name__ == "__main__":
    print(
        Solution().mergeKLists(
            [
                ListNode.init_by_lst([1, 4, 5]),
                ListNode.init_by_lst([1, 3, 4]),
                ListNode.init_by_lst([2, 6]),
            ]
        )
    )
