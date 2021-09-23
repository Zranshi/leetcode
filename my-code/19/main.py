# -*- coding: UTF-8 -*-
# @Time     : 2021/08/30 08:13
# @Author   : Ranshi
# @File     : main.py
class ListNode:
    def __init__(self, next: "ListNode", val=0):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        new_head = ListNode(val=-1, next=head)
        fast, slow = new_head, new_head
        while fast.next:
            if n != 0:
                n -= 1
            else:
                slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return new_head.next


if __name__ == "__main__":
    ...
