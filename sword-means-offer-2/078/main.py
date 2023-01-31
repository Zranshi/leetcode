# -*- coding: UTF-8 -*-
# @Time     : 2023/01/22 22:50
# @Author   : Ranshi
# @File     : main.py
# @Doc      : 剑指 Offer II 078. 合并排序链表
from typing import List

from type.list_node import ListNode


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode | None:
        if len(lists) == 0:
            return None
        elif len(lists) == 1:

            return lists[0]
        elif len(lists) == 2:
            return self.merge(lists[0], lists[1])
        return self.merge(
            self.mergeKLists(lists[: len(lists) // 2]),
            self.mergeKLists(lists[len(lists) // 2:]),
        )

    def merge(self, l1: ListNode, l2: ListNode):
        dummy_head = ListNode()
        p = dummy_head
        while l1 and l2:
            if l1.val < l2.val:
                l1, p.next = l1.next, l1
            else:
                l2, p.next = l2.next, l2
            p = p.next
        if l1:
            p.next = l1
        elif l2:
            p.next = l2
        return dummy_head.next


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
