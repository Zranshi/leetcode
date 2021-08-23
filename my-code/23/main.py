# -*- coding: UTF-8 -*-
# @Time     : 2021/08/21 21:24
# @Author   : Ranshi
# @File     : main.py

from typing import List


class ListNode:

    def __init__(self, val=0, next: 'ListNode' = None):
        self.val = val
        self.next = next


class Solution:

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        import heapq
        q = [(lists[idx].val, idx) for idx in range(len(lists))]
        heapq.heapify(q)
        new_head = ListNode()
        tail = 


if __name__ == '__main__':
    ...
