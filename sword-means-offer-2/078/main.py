# -*- coding: UTF-8 -*-
# @Time     : 2023/01/22 22:50
# @Author   : Ranshi
# @File     : main.py
# @Doc      : 剑指 Offer II 078. 合并排序链表
from typing import List

from type.list_node import ListNode


# class Solution:
#     def mergeKLists(self, lists: List[ListNode]) -> ListNode:
#         if len(lists) == 0:
#             return None
#         dummy_head = ListNode()
#         p = dummy_head
#         while True:
#             _min = 0
#             for i in range(0, len(lists)):
#                 if lists[_min] is None or (
#                     lists[i] is not None and lists[_min].val > lists[i].val
#                 ):
#                     _min = i
#             if lists[_min] is None:
#                 break
#             p.next = lists[_min]
#             lists[_min].next, lists[_min] = None, lists[_min].next
#             p = p.next
#         print(dummy_head)
#         return dummy_head.next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        ...


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
