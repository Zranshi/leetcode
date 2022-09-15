# -*- coding: UTF-8 -*-
# @Time     : 2022/09/15 13:37
# @Author   : Ranshi
# @File     : main.py
# @Doc      : 剑指 Offer II 027. 回文链表

from type.list_node import ListNode


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        vals = []
        current_node = head
        while current_node is not None:
            vals.append(current_node.val)
            current_node = current_node.next
        return vals == vals[::-1]


if __name__ == "__main__":
    print(Solution().isPalindrome(ListNode.init_by_lst([1, 2, 3, 3, 2, 1])))
