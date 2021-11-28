#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     : 2021/11/14 10:38
# @Author   : Ranshi
# @File     : main.py
# @Doc      : 5927. 反转偶数长度组的节点
from typing import Optional

from pyal.container import ListNode


class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 1
        idx = 0
        new_head = ListNode(next=head)
        cur = new_head

        def reverse_list_node(node: ListNode, length: int):
            cur, idx_num = node, 0
            while cur and idx_num < length:
                idx_num += 1
                cur = cur.next
            head = ListNode(next=cur)
            cur, idx_num = node, 0
            while cur and idx_num < length:
                idx_num += 1
                tmp = head.next
                head.next, cur = cur, cur.next
                head.next.next = tmp
            return head.next

        while cur.next:
            idx = 0
            tmp_cur = cur
            while tmp_cur.next and idx < length:
                idx += 1
                tmp_cur = tmp_cur.next
            idx_length = idx
            idx = 0

            if idx_length % 2 == 0:
                cur.next = reverse_list_node(cur.next, idx_length)
            while cur.next and idx < length:
                cur = cur.next
                idx += 1
            length += 1
        return new_head.next


if __name__ == "__main__":
    print(Solution().reverseEvenLengthGroups(head=ListNode.init_by_lst([0, 4, 2, 1, 3])))
