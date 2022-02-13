# -*- coding: UTF-8 -*-
# @Time     : 2021/10/03 21:51
# @Author   : Ranshi
# @File     : 123.py
from type.list_node import ListNode


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        new_head = ListNode()
        p, p1, p2 = new_head, l1, l2
        while p1 and p2:
            if p1.val <= p2.val:
                p1, p.next = p1.next, p1
            else:
                p2, p.next = p2.next, p2
            p = p.next
        p.next = p1 or p2
        return new_head.next


if __name__ == "__main__":
    print(
        Solution().mergeTwoLists(
            l1=ListNode.init_by_lst([1, 2, 4]),
            l2=ListNode.init_by_lst([1, 3, 4]),
        )
    )
