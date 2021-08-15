# -*- coding: UTF-8 -*-
# @Time     : 2021/08/15 08:47
# @Author   : Ranshi
# @File     : main.py


class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1 = ''
        while l1 is not None:
            s1 = s1 + str(l1.val)
            l1 = l1.next
        s2 = ''
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


if __name__ == '__main__':
    ...
