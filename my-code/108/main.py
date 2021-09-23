# -*- coding: UTF-8 -*-
# @Time     : 2021/08/19 08:08
# @Author   : Ranshi
# @File     : main.py

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left: "TreeNode" = None, right: "TreeNode" = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def merge(le, ri) -> Optional[TreeNode]:
            if le == ri:
                return TreeNode(val=nums[le])
            if le > ri:
                return None
            mid = (le + ri) // 2
            return TreeNode(
                val=nums[mid],
                left=merge(le, mid - 1),
                right=merge(mid + 1, ri),
            )

        return merge(0, len(nums) - 1)


if __name__ == "__main__":
    print(Solution().sortedArrayToBST(nums=[-10, -3, 0, 5, 9]))
