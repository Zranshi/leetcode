#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time     : 2021/10/09 12:21
# @Author   : Ranshi
# @File     : main.py
from type.tree_node import TreeNode


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return max(
            self.maxDepth(root.left) + 1 if root.left else 1,
            self.maxDepth(root.right) + 1 if root.right else 1,
        )


if __name__ == "__main__":
    print(Solution().maxDepth(TreeNode.init_by_list([1, 2])))
