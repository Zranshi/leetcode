# -*- coding: UTF-8 -*-
# @Time     : 2021/09/02 22:04
# @Author   : Ranshi
# @File     : main.py

from type.list_node import ListNode


class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        fast = head
        slow = head
        for _ in range(k):
            fast = fast.next
        while fast:
            fast = fast.next
            slow = slow.next
        return slow


if __name__ == "__main__":
    print(Solution().getKthFromEnd(ListNode.init_by_lst([1, 2, 3, 4, 5]), 2))
