#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     : 2021/12/06 20:11
# @Author   : Ranshi
# @File     : main.py
# @Doc      : 2. 两数相加
from pyal.container import ListNode


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1 = ""
        while l1 is not None:
            s1 = s1 + str(l1.val)
            l1 = l1.next
        s2 = ""
        while l2 is not None:
            s2 = s2 + str(l2.val)
            l2 = l2.next
        s3 = int(s1[::-1]) + int(s2[::-1])
        s3 = [int(i) for i in str(s3)][::-1]
        root = ListNode(s3.pop(0))
        current = root
        while s3 != []:
            current.next = ListNode(s3.pop(0))
            current = current.next
        return root


if __name__ == "__main__":
    print(
        Solution().addTwoNumbers(
            l1=ListNode.init_by_lst([2, 4, 3]), l2=ListNode.init_by_lst([5, 6, 4])
        )
    )
