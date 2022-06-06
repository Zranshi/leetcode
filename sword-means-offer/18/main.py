# -*- coding: UTF-8 -*-
# @Time     : 2021/10/02 21:32
# @Author   : Ranshi
# @File     : 123.py
from type.list_node import ListNode


class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        new_head = ListNode(0, next_=head)
        cur: "ListNode" = new_head
        while cur and cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            cur = cur.next
        return new_head.next


if __name__ == "__main__":
    print(Solution().deleteNode(head=ListNode.init_by_lst([4, 5, 1, 9]), val=1))
