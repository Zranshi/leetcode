# -*- coding: UTF-8 -*-
# @Time     : 2021/09/22 07:39
# @Author   : Ranshi
# @File     : 123.py
from typing import List

from type.list_node import ListNode


class Solution:
    def splitListToParts(self, head: ListNode, k: int) -> List[ListNode]:
        cur, left = head, 0
        while cur:
            left += 1
            cur = cur.next
        each, remain = left // k, left % k
        cur, ans, idx = head, [None] * k, 0
        while cur:
            ans[idx] = cur
            last = None
            for i in range(each + (idx < remain)):
                last = cur
                cur = cur.next
            idx += 1
            last.next = None
        return ans


if __name__ == "__main__":
    print(Solution().splitListToParts(head=ListNode.init_by_lst([1, 2, 3]), k=5))
