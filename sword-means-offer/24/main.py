# -*- coding: UTF-8 -*-
# @Time     : 2021/09/25 07:26
# @Author   : Ranshi
# @File     : 123.py
from type.list_node import ListNode


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        new_head = ListNode()
        new_cur = new_head
        cur = head
        while cur:
            idx = cur
            cur = cur.next
            idx.next = new_cur.next
            new_cur.next = idx
        return new_head.next


if __name__ == "__main__":
    print(Solution().reverseList(ListNode.init_by_lst([1, 2, 3, 4, 5])))
