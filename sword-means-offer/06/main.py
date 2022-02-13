# -*- coding: UTF-8 -*-
# @Time     : 2021/09/25 07:23
# @Author   : Ranshi
# @File     : 123.py
from typing import List

from type.list_node import ListNode


class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        res = []
        cur = head
        while cur:
            res.append(cur.val)
            cur = cur.next
        return res[::-1]


if __name__ == "__main__":
    print(Solution().reversePrint(ListNode.init_by_lst([1, 3, 2])))
