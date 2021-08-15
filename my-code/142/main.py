# -*- coding: UTF-8 -*-
# @Time     : 2021/08/15 08:50
# @Author   : Ranshi
# @File     : main.py


class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def detectCycle(self, head):
        fast, slow = head, head
        while True:
            if not (fast and fast.next):
                return
            fast, slow = fast.next.next, slow.next
            if fast == slow:
                break
        fast = head
        while fast != slow:
            fast, slow = fast.next, slow.next
        return fast


if __name__ == '__main__':
    ...
